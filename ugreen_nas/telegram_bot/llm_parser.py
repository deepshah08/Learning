"""
Natural Language Parser & Intent Extraction Engine for Media Requests.
Uses LLM (Gemini / Claude / OpenAI) with robust regex/heuristic fallback.
"""
import re
import json
from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class MediaRequest(BaseModel):
    title: str = Field(description="Clean title of the movie or TV show, with typos corrected.")
    media_type: Literal["movie", "series", "unknown"] = Field(
        default="unknown",
        description="Whether the request is for a movie, a TV series, or unknown."
    )
    year: Optional[int] = Field(default=None, description="Release year if specified.")
    season: Optional[int] = Field(default=None, description="Season number if requested for a TV series (e.g., 4 for Season 4).")
    episodes: Optional[List[int]] = Field(default=None, description="List of specific episode numbers (e.g. [1,2,3]) or None for entire season/all.")
    is_season_pack: bool = Field(default=False, description="True if the request explicitly asks for a full season batch/pack.")
    resolution: Literal["4K", "1080p", "720p", "any"] = Field(default="1080p", description="Requested video resolution.")
    preferred_audio: List[str] = Field(default_factory=lambda: ["Hindi", "English"], description="Audio language preferences in priority order.")
    embedded_subtitles: bool = Field(default=True, description="Whether subtitles are requested or preferred.")
    raw_query: str = Field(default="", description="Original unparsed text.")


SYSTEM_PROMPT = """You are a specialized Media Request Parser for a home lab media automation system (Plex, Radarr, Sonarr, Prowlarr).
Given a user query in natural language, extract and normalize the requested movie or series into a structured JSON object.

Rules:
1. Auto-correct obvious spelling mistakes in movie/series titles (e.g. "stranger thing" -> "Stranger Things", "incepton" -> "Inception").
2. Detect if it is a TV series (mentions seasons, episodes, 's1', 's04', 'series', 'show') vs a movie.
3. If a season is requested without specific episode numbers, set is_season_pack = true.
4. If specific episode ranges are requested (e.g., "episodes 1 to 5" or "e1-e5"), extract them as an integer list: [1, 2, 3, 4, 5].
5. Detect requested resolution (4K / 2160p -> "4K", 1080p / FHD -> "1080p", 720p / HD -> "720p"). Default to "1080p" if unspecified.
6. Detect language preferences (Hindi, English, Tamil, Telugu, Dual Audio). If Hindi is mentioned, place Hindi first in preferred_audio. Default to ["Hindi", "English"].
7. Subtitles: Default to true unless explicitly disabled.

Respond ONLY with a valid JSON object matching this schema:
{
  "title": "Stranger Things",
  "media_type": "series",
  "year": null,
  "season": 4,
  "episodes": null,
  "is_season_pack": true,
  "resolution": "1080p",
  "preferred_audio": ["Hindi", "English"],
  "embedded_subtitles": true
}"""


def parse_with_heuristics(query: str) -> MediaRequest:
    """Robust regex-based fallback parser when LLM API key is not yet provided."""
    clean_query = query.strip()
    media_type: Literal["movie", "series", "unknown"] = "unknown"
    season: Optional[int] = None
    episodes: Optional[List[int]] = None
    is_season_pack = False
    resolution: Literal["4K", "1080p", "720p", "any"] = "1080p"
    preferred_audio = ["Hindi", "English"]

    # Resolution detection
    if re.search(r"\b(4k|2160p|uhd)\b", clean_query, re.I):
        resolution = "4K"
    elif re.search(r"\b(1080p|fhd|full hd)\b", clean_query, re.I):
        resolution = "1080p"
    elif re.search(r"\b(720p|hd)\b", clean_query, re.I):
        resolution = "720p"

    # Audio preference detection
    if re.search(r"\bhindi\b", clean_query, re.I):
        preferred_audio = ["Hindi", "English"]
    elif re.search(r"\benglish\b", clean_query, re.I) and not re.search(r"\bhindi\b", clean_query, re.I):
        preferred_audio = ["English"]

    # 1. Season Extraction
    season_match = re.search(r"\b(?:s|season)\s*(\d+)\b", clean_query, re.I)
    if season_match:
        media_type = "series"
        season = int(season_match.group(1))
        is_season_pack = True

    # 2. Episode Range Extraction (e.g. episodes 1 to 4 or e01-08)
    ep_range_match = re.search(r"\b(?:e|ep|episodes?)\s*(\d+)\s*(?:-|to)\s*(\d+)\b", clean_query, re.I)
    if ep_range_match:
        media_type = "series"
        start_ep = int(ep_range_match.group(1))
        end_ep = int(ep_range_match.group(2))
        episodes = list(range(start_ep, end_ep + 1))
        is_season_pack = False
    else:
        # Specific single episode: e05 or ep 5
        ep_single_match = re.search(r"\b(?:e|ep|episode)\s*(\d+)\b", clean_query, re.I)
        if ep_single_match:
            media_type = "series"
            episodes = [int(ep_single_match.group(1))]
            is_season_pack = False

    # Extract title by stripping keywords
    title_candidate = clean_query
    # Strip command prefixes
    title_candidate = re.sub(r"^(?:download|get|find|fetch|search for|pull|add)\s+", "", title_candidate, flags=re.I)
    # Strip season/ep tokens
    title_candidate = re.sub(r"\b(?:season\s*\d+|s\d+|episodes?\s*\d+\s*(?:to|-)\s*\d+|episodes?\s*\d+|ep\s*\d+|e\d+)\b", "", title_candidate, flags=re.I)
    # Strip resolution tokens
    title_candidate = re.sub(r"\b(?:4k|2160p|1080p|720p|fhd|uhd|hd)\b", "", title_candidate, flags=re.I)
    # Strip language tokens
    title_candidate = re.sub(r"\b(?:hindi|english|dual audio|multi audio|audio|subtitles|subs)\b", "", title_candidate, flags=re.I)
    # Strip trailing/leading preposition stop words
    title_candidate = re.sub(r"\b(?:in|with|for|and|the)\b\s*$", "", title_candidate, flags=re.I)
    title_candidate = re.sub(r"\s+\b(?:in|with|for)\b\s*.*$", "", title_candidate, flags=re.I)
    # Clean non-alphanumeric punctuation
    title_candidate = re.sub(r"[^\w\s-]", "", title_candidate).strip()

    if not title_candidate:
        title_candidate = clean_query

    # Title casing & auto-corrections for common franchises
    title_lower = title_candidate.lower()
    if "stranger thing" in title_lower:
        title_candidate = "Stranger Things"
        media_type = "series"
    elif "game of throne" in title_lower or "got" == title_lower:
        title_candidate = "Game of Thrones"
        media_type = "series"
    elif "house of the dragon" in title_lower or "hotd" == title_lower:
        title_candidate = "House of the Dragon"
        media_type = "series"
    elif "breaking bad" in title_lower:
        title_candidate = "Breaking Bad"
        media_type = "series"
    elif "interstellar" in title_lower:
        title_candidate = "Interstellar"
        media_type = "movie"
    elif "inception" in title_lower:
        title_candidate = "Inception"
        media_type = "movie"
    else:
        title_candidate = title_candidate.title()

    if media_type == "unknown":
        if season is not None or episodes is not None:
            media_type = "series"
        else:
            media_type = "movie"

    return MediaRequest(
        title=title_candidate,
        media_type=media_type,
        season=season,
        episodes=episodes,
        is_season_pack=is_season_pack,
        resolution=resolution,
        preferred_audio=preferred_audio,
        embedded_subtitles=True,
        raw_query=query
    )


async def parse_media_query(query: str, api_key: Optional[str] = None) -> MediaRequest:
    """Parses user natural language query using LLM (if key available) or heuristic fallback."""
    if not api_key:
        return parse_with_heuristics(query)

    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        
        prompt = f"{SYSTEM_PROMPT}\n\nUser Query: \"{query}\"\nJSON Output:"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        
        raw_text = response.text.strip()
        # Clean markdown codeblocks if wrapped
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
            
        data = json.loads(raw_text.strip())
        data["raw_query"] = query
        return MediaRequest(**data)
    except Exception as e:
        # Fallback cleanly on any API or network issue
        return parse_with_heuristics(query)
