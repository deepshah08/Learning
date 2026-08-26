"""
Configuration module for Telegram Media Automation Bot.
Loads environment variables with strict type validation using Pydantic Settings.
"""
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class BotConfig(BaseSettings):
    # Telegram Credentials
    telegram_bot_token: str = Field(default="", alias="TELEGRAM_BOT_TOKEN")
    allowed_user_ids: List[int] = Field(default_factory=list, alias="ALLOWED_USER_IDS")

    # LLM Settings (for Natural Language Extraction)
    llm_api_key: Optional[str] = Field(default=None, alias="LLM_API_KEY")
    llm_provider: str = Field(default="gemini", alias="LLM_PROVIDER") # gemini, openai, fallback
    llm_model: str = Field(default="gemini-2.0-flash", alias="LLM_MODEL")

    # Arr Stack Endpoints & API Keys (Defaults pre-configured for UGREEN NAS network)
    radarr_url: str = Field(default="http://192.168.1.80:7878", alias="RADARR_URL")
    radarr_api_key: str = Field(default="30ad1ab196a04184b11289e39a695f20", alias="RADARR_API_KEY")

    sonarr_url: str = Field(default="http://192.168.1.80:8989", alias="SONARR_URL")
    sonarr_api_key: str = Field(default="7385f68a846a416d9964d08d1eccda12", alias="SONARR_API_KEY")

    prowlarr_url: str = Field(default="http://192.168.1.80:9696", alias="PROWLARR_URL")
    prowlarr_api_key: str = Field(default="eb674050f3e24beaa54b515dbb7a01ac", alias="PROWLARR_API_KEY")

    # Plex / Notification Settings
    plex_url: str = Field(default="http://192.168.1.80:32400", alias="PLEX_URL")
    plex_token: Optional[str] = Field(default=None, alias="PLEX_TOKEN")

    # Storage & Root Folders
    movies_root_folder: str = Field(default="/data/media/movies", alias="MOVIES_ROOT_FOLDER")
    tv_root_folder: str = Field(default="/data/media/tv", alias="TV_ROOT_FOLDER")

    # Default Quality Profiles
    default_quality_profile_id: int = Field(default=1, alias="DEFAULT_QUALITY_PROFILE_ID")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# Singleton instance
config = BotConfig()
