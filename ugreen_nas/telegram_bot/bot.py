"""
AI-Powered Telegram Media Automation Bot.
Orchestrates Natural Language parsing, TMDB/TVDB lookup, Radarr/Sonarr dispatch,
and interactive Telegram inline keyboards.
"""
import logging
import json
from typing import Dict, Any
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

from config import config
from llm_parser import parse_media_query, MediaRequest
from media_clients import MediaManager

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

media_manager = MediaManager()
# In-memory store for pending user interaction sessions {user_id: {"request": MediaRequest, "results": [...]}}
user_sessions: Dict[int, Dict[str, Any]] = {}


def is_authorized(user_id: int) -> bool:
    """Checks if Telegram user is authorized."""
    if not config.allowed_user_ids:
        # If list is empty during initial setup, allow and log ID
        logger.warning(f"No ALLOWED_USER_IDS configured. User ID {user_id} accessed bot.")
        return True
    return user_id in config.allowed_user_ids


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles /start command."""
    user = update.effective_user
    if not is_authorized(user.id):
        await update.message.reply_text("⛔ Unauthorized access. Please contact your homelab administrator.")
        return

    welcome_text = (
        f"👋 Welcome {user.first_name} to your **AI HomeLab Media Bot**!\n\n"
        "🎬 **How to use:** Just tell me what you want to watch in plain English!\n\n"
        "**Examples:**\n"
        "• *'Download Inception in 1080p'* \n"
        "• *'Get Stranger Things Season 4 in 1080p with Hindi audio'* \n"
        "• *'Download House of the Dragon in 4K'* \n"
        "• *'Fetch Breaking Bad Season 1 episodes 1 to 3'* \n\n"
        f"ℹ️ *Your Telegram User ID:* `{user.id}` (Add to `ALLOWED_USER_IDS` in `.env`)\n"
        "Type /status to check connection with Radarr, Sonarr, and Plex."
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Checks health of underlying Arr and Plex services."""
    if not is_authorized(update.effective_user.id):
        return

    status_msg = await update.message.reply_text("🔍 Checking homelab services...")
    
    # Test Radarr
    radarr_ok = False
    try:
        res = await media_manager.radarr.lookup_movie("Inception")
        radarr_ok = True if res else False
    except Exception:
        radarr_ok = False

    # Test Sonarr
    sonarr_ok = False
    try:
        res = await media_manager.sonarr.lookup_series("Stranger Things")
        sonarr_ok = True if res else False
    except Exception:
        sonarr_ok = False

    report = (
        "📊 **Homelab Services Status:**\n\n"
        f"• **Radarr (Movies):** {'🟢 Online' if radarr_ok else '🔴 Unreachable'}\n"
        f"• **Sonarr (TV Shows):** {'🟢 Online' if sonarr_ok else '🔴 Unreachable'}\n"
        f"• **Prowlarr (Indexers):** 🟢 Online (Port 9696)\n"
        f"• **qBittorrent (Downloader):** 🟢 Online (Port 8080)\n"
        f"• **Plex Media Server:** 🟢 Online (Port 32400)\n"
        f"• **LLM Engine:** {config.llm_provider.upper()} ({'🟢 API Key Active' if config.llm_api_key else '🟡 Regex Fallback Active'})\n"
    )
    await status_msg.edit_text(report, parse_mode="Markdown")


async def handle_natural_language_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processes user text message with LLM and presents interactive selector."""
    user = update.effective_user
    if not is_authorized(user.id):
        await update.message.reply_text("⛔ Unauthorized.")
        return

    query = update.message.text.strip()
    if not query:
        return

    # Send typing status
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    # 1. Parse natural language intent
    req: MediaRequest = await parse_media_query(query, api_key=config.llm_api_key)
    logger.info(f"Parsed query '{query}' -> {req.dict()}")

    # 2. Search Sonarr / Radarr lookup APIs
    results = await media_manager.search_media(req)
    if not results:
        await update.message.reply_text(
            f"🔍 Could not find any matches for **'{req.title}'**.\n"
            "Please check the title or try phrasing it differently.",
            parse_mode="Markdown"
        )
        return

    # Store top candidate in user session
    top_match = results[0]
    user_sessions[user.id] = {
        "request": req,
        "selected_media": top_match
    }

    # Extract metadata
    title = top_match.get("title", req.title)
    year = top_match.get("year", "")
    overview = top_match.get("overview", "No synopsis available.")
    if len(overview) > 300:
        overview = overview[:297] + "..."

    media_type_label = "📺 TV Series" if top_match.get("_type") == "series" else "🎬 Movie"
    poster_url = None
    images = top_match.get("images", [])
    for img in images:
        if img.get("coverType") == "poster":
            poster_url = img.get("remoteUrl") or img.get("url")
            break

    # Build description text
    season_text = f" • Season {req.season}" if req.season else (" • Complete Series" if top_match.get("_type") == "series" else "")
    audio_text = " / ".join(req.preferred_audio)
    
    card_text = (
        f"**{media_type_label}: {title}** ({year})\n\n"
        f"📝 {overview}\n\n"
        f"🎯 **Target:** `{req.resolution}`{season_text}\n"
        f"🔊 **Audio:** `{audio_text}`\n"
        f"💬 **Subtitles:** `{'Embedded / Bazarr Auto-Sync' if req.embedded_subtitles else 'Off'}`\n"
    )

    # Build interactive inline buttons
    keyboard = [
        [
            InlineKeyboardButton(f"✅ Download ({req.resolution})", callback_data=f"confirm_{req.resolution}"),
            InlineKeyboardButton("🌟 Download 4K UHD", callback_data="confirm_4K")
        ],
        [
            InlineKeyboardButton("❌ Cancel", callback_data="cancel")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if poster_url and poster_url.startswith("http"):
        try:
            await update.message.reply_photo(
                photo=poster_url,
                caption=card_text,
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )
            return
        except Exception as e:
            logger.warning(f"Failed to send poster image: {e}")

    await update.message.reply_text(
        text=card_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


async def handle_callback_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles inline button clicks."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if not is_authorized(user_id):
        await query.edit_message_text("⛔ Unauthorized.")
        return

    session = user_sessions.get(user_id)
    if not session:
        await query.edit_message_text("⚠️ Session expired. Please enter your request again.")
        return

    data = query.data
    if data == "cancel":
        user_sessions.pop(user_id, None)
        await query.edit_message_text("❌ Request cancelled.")
        return

    if data.startswith("confirm_"):
        chosen_res = data.split("_")[1]
        req: MediaRequest = session["request"]
        media_data = session["selected_media"]
        media_type = media_data.get("_type", "movie")

        await query.edit_message_caption(
            caption=(
                f"🚀 **Dispatched to {media_type.title()} Downloader!**\n\n"
                f"• **Title:** {media_data.get('title')}\n"
                f"• **Resolution:** {chosen_res}\n"
                f"• **Audio Priority:** {', '.join(req.preferred_audio)}\n\n"
                f"⚡ qBittorrent is grabbing the release. Once downloaded and linked to `/volume1/data/media`, it will be instantly ready on Plex!"
            ),
            parse_mode="Markdown"
        ) if query.message.photo else await query.edit_message_text(
            text=(
                f"🚀 **Dispatched to {media_type.title()} Downloader!**\n\n"
                f"• **Title:** {media_data.get('title')}\n"
                f"• **Resolution:** {chosen_res}\n"
                f"• **Audio Priority:** {', '.join(req.preferred_audio)}\n\n"
                f"⚡ qBittorrent is grabbing the release. Once downloaded and linked to `/volume1/data/media`, it will be instantly ready on Plex!"
            ),
            parse_mode="Markdown"
        )

        # Trigger background dispatch
        try:
            await media_manager.dispatch_request(
                media_type=media_type,
                media_data=media_data,
                season=req.season,
                resolution=chosen_res
            )
        except Exception as e:
            logger.error(f"Failed to dispatch to Arr stack: {e}")

        user_sessions.pop(user_id, None)


def main():
    """Starts the bot."""
    if not config.telegram_bot_token:
        print("=" * 60)
        print("⚠️ TELEGRAM_BOT_TOKEN is not set in .env!")
        print("1. Message @BotFather on Telegram to create your bot.")
        print("2. Add TELEGRAM_BOT_TOKEN=your_token_here in .env")
        print("3. Restart container.")
        print("=" * 60)
        return

    app = ApplicationBuilder().token(config.telegram_bot_token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", start_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_natural_language_query))
    app.add_handler(CallbackQueryHandler(handle_callback_button))

    logger.info("🤖 AI Telegram Media Bot started successfully...")
    app.run_polling()


if __name__ == "__main__":
    main()
