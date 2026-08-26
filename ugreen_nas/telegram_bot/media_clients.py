"""
Asynchronous API client integration for Radarr, Sonarr, Prowlarr, and Plex.
"""
import httpx
from typing import List, Dict, Any, Optional
from config import config
from llm_parser import MediaRequest


class RadarrClient:
    def __init__(self, base_url: str = config.radarr_url, api_key: str = config.radarr_api_key):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {"X-Api-Key": self.api_key}

    async def lookup_movie(self, title: str) -> List[Dict[str, Any]]:
        """Search for movies by title via Radarr lookup API."""
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(
                f"{self.base_url}/api/v3/movie/lookup",
                params={"term": title},
                headers=self.headers
            )
            if resp.status_code == 200:
                return resp.json()
            return []

    async def add_movie(
        self,
        movie_data: Dict[str, Any],
        quality_profile_id: int = 1,
        root_folder_path: str = config.movies_root_folder,
        search_now: bool = True
    ) -> Dict[str, Any]:
        """Add movie to Radarr library and trigger search."""
        payload = {
            "title": movie_data.get("title"),
            "qualityProfileId": quality_profile_id,
            "titleSlug": movie_data.get("titleSlug"),
            "images": movie_data.get("images", []),
            "tmdbId": movie_data.get("tmdbId"),
            "year": movie_data.get("year"),
            "rootFolderPath": root_folder_path,
            "monitored": True,
            "addOptions": {
                "searchForMovie": search_now
            }
        }
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(
                f"{self.base_url}/api/v3/movie",
                json=payload,
                headers=self.headers
            )
            return resp.json()


class SonarrClient:
    def __init__(self, base_url: str = config.sonarr_url, api_key: str = config.sonarr_api_key):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {"X-Api-Key": self.api_key}

    async def lookup_series(self, title: str) -> List[Dict[str, Any]]:
        """Search for TV series by title via Sonarr lookup API."""
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(
                f"{self.base_url}/api/v3/series/lookup",
                params={"term": title},
                headers=self.headers
            )
            if resp.status_code == 200:
                return resp.json()
            return []

    async def add_series(
        self,
        series_data: Dict[str, Any],
        season_number: Optional[int] = None,
        quality_profile_id: int = 1,
        root_folder_path: str = config.tv_root_folder,
        search_now: bool = True
    ) -> Dict[str, Any]:
        """Add TV series to Sonarr library with selective season monitoring."""
        seasons = series_data.get("seasons", [])
        if season_number is not None:
            # Monitor ONLY the requested season
            for s in seasons:
                s["monitored"] = (s.get("seasonNumber") == season_number)

        payload = {
            "title": series_data.get("title"),
            "qualityProfileId": quality_profile_id,
            "titleSlug": series_data.get("titleSlug"),
            "images": series_data.get("images", []),
            "tvdbId": series_data.get("tvdbId"),
            "year": series_data.get("year"),
            "rootFolderPath": root_folder_path,
            "monitored": True,
            "seasons": seasons,
            "addOptions": {
                "searchForMissingEpisodes": search_now
            }
        }
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(
                f"{self.base_url}/api/v3/series",
                json=payload,
                headers=self.headers
            )
            return resp.json()


class MediaManager:
    """Unified facade managing lookup and dispatch across Radarr and Sonarr."""
    def __init__(self):
        self.radarr = RadarrClient()
        self.sonarr = SonarrClient()

    async def search_media(self, req: MediaRequest) -> List[Dict[str, Any]]:
        """Searches Radarr or Sonarr based on parsed media type."""
        results = []
        if req.media_type in ("series", "unknown"):
            series_res = await self.sonarr.lookup_series(req.title)
            for s in series_res:
                s["_type"] = "series"
                results.append(s)

        if req.media_type in ("movie", "unknown") and len(results) < 5:
            movie_res = await self.radarr.lookup_movie(req.title)
            for m in movie_res:
                m["_type"] = "movie"
                results.append(m)

        return results[:5]

    async def dispatch_request(
        self,
        media_type: str,
        media_data: Dict[str, Any],
        season: Optional[int] = None,
        resolution: str = "1080p"
    ) -> Dict[str, Any]:
        """Dispatches approved download to the appropriate Arr service."""
        # Quality profile mapping: 1 = Standard 1080p, adjust as needed in Sonarr/Radarr
        quality_profile_id = 1

        if media_type == "series":
            return await self.sonarr.add_series(
                series_data=media_data,
                season_number=season,
                quality_profile_id=quality_profile_id,
                search_now=True
            )
        else:
            return await self.radarr.add_movie(
                movie_data=media_data,
                quality_profile_id=quality_profile_id,
                search_now=True
            )
