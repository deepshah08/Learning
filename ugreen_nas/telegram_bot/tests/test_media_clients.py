import os
import sys
import pytest
from unittest.mock import AsyncMock, patch, MagicMock

# Ensure parent directory is in python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from media_clients import RadarrClient, SonarrClient, MediaManager
from llm_parser import MediaRequest
from config import config

@pytest.fixture
def radarr_client():
    return RadarrClient(base_url="http://mock-radarr:7878", api_key="radarr-key")

@pytest.fixture
def sonarr_client():
    return SonarrClient(base_url="http://mock-sonarr:8989", api_key="sonarr-key")

@pytest.fixture
def media_manager():
    return MediaManager()

# --- RadarrClient Tests ---

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_radarr_lookup_movie_success(mock_client_class, radarr_client):
    mock_client = AsyncMock()
    mock_client_class.return_value.__aenter__.return_value = mock_client

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"title": "Inception", "year": 2010}]
    mock_client.get.return_value = mock_response

    result = await radarr_client.lookup_movie("Inception")

    assert len(result) == 1
    assert result[0]["title"] == "Inception"
    mock_client.get.assert_called_once_with(
        "http://mock-radarr:7878/api/v3/movie/lookup",
        params={"term": "Inception"},
        headers={"X-Api-Key": "radarr-key"}
    )

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_radarr_lookup_movie_failure(mock_client_class, radarr_client):
    mock_client = AsyncMock()
    mock_client_class.return_value.__aenter__.return_value = mock_client

    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_client.get.return_value = mock_response

    result = await radarr_client.lookup_movie("NonExistent")

    assert result == []

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_radarr_add_movie(mock_client_class, radarr_client):
    mock_client = AsyncMock()
    mock_client_class.return_value.__aenter__.return_value = mock_client

    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "title": "Inception"}
    mock_client.post.return_value = mock_response

    movie_data = {"title": "Inception", "titleSlug": "inception", "tmdbId": 123, "year": 2010}
    result = await radarr_client.add_movie(movie_data, root_folder_path="/movies")

    assert result["title"] == "Inception"
    mock_client.post.assert_called_once()
    args, kwargs = mock_client.post.call_args
    assert kwargs["json"]["title"] == "Inception"
    assert kwargs["json"]["rootFolderPath"] == "/movies"
    assert kwargs["json"]["monitored"] is True

# --- SonarrClient Tests ---

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_sonarr_lookup_series_success(mock_client_class, sonarr_client):
    mock_client = AsyncMock()
    mock_client_class.return_value.__aenter__.return_value = mock_client

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"title": "Breaking Bad"}]
    mock_client.get.return_value = mock_response

    result = await sonarr_client.lookup_series("Breaking Bad")

    assert len(result) == 1
    assert result[0]["title"] == "Breaking Bad"
    mock_client.get.assert_called_once_with(
        "http://mock-sonarr:8989/api/v3/series/lookup",
        params={"term": "Breaking Bad"},
        headers={"X-Api-Key": "sonarr-key"}
    )

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_sonarr_lookup_series_failure(mock_client_class, sonarr_client):
    mock_client = AsyncMock()
    mock_client_class.return_value.__aenter__.return_value = mock_client

    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_client.get.return_value = mock_response

    result = await sonarr_client.lookup_series("ErrorShow")

    assert result == []

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_sonarr_add_series_all_seasons(mock_client_class, sonarr_client):
    mock_client = AsyncMock()
    mock_client_class.return_value.__aenter__.return_value = mock_client

    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "title": "Breaking Bad"}
    mock_client.post.return_value = mock_response

    series_data = {
        "title": "Breaking Bad",
        "seasons": [{"seasonNumber": 1}, {"seasonNumber": 2}]
    }
    result = await sonarr_client.add_series(series_data, root_folder_path="/tv")

    assert result["title"] == "Breaking Bad"
    mock_client.post.assert_called_once()
    args, kwargs = mock_client.post.call_args
    # Both seasons should remain in their default state in this case
    # (The function doesn't actually set monitored if season_number is None)
    assert len(kwargs["json"]["seasons"]) == 2

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_sonarr_add_series_specific_season(mock_client_class, sonarr_client):
    mock_client = AsyncMock()
    mock_client_class.return_value.__aenter__.return_value = mock_client

    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "title": "Breaking Bad"}
    mock_client.post.return_value = mock_response

    series_data = {
        "title": "Breaking Bad",
        "seasons": [{"seasonNumber": 1}, {"seasonNumber": 2}]
    }
    result = await sonarr_client.add_series(series_data, season_number=2, root_folder_path="/tv")

    mock_client.post.assert_called_once()
    args, kwargs = mock_client.post.call_args
    seasons = kwargs["json"]["seasons"]
    assert seasons[0]["seasonNumber"] == 1
    assert seasons[0]["monitored"] is False
    assert seasons[1]["seasonNumber"] == 2
    assert seasons[1]["monitored"] is True

# --- MediaManager Tests ---

@pytest.mark.asyncio
@patch.object(SonarrClient, 'lookup_series')
@patch.object(RadarrClient, 'lookup_movie')
async def test_media_manager_search_media_unknown(mock_lookup_movie, mock_lookup_series, media_manager):
    mock_lookup_series.return_value = [{"title": "Series A"}]
    mock_lookup_movie.return_value = [{"title": "Movie A"}]

    req = MediaRequest(title="Test", media_type="unknown", is_season_pack=False, episodes=[], preferred_audio=[], resolution="1080p")
    results = await media_manager.search_media(req)

    assert len(results) == 2
    assert results[0]["title"] == "Series A"
    assert results[0]["_type"] == "series"
    assert results[1]["title"] == "Movie A"
    assert results[1]["_type"] == "movie"

@pytest.mark.asyncio
@patch.object(RadarrClient, 'lookup_movie')
@patch.object(SonarrClient, 'lookup_series')
async def test_media_manager_search_media_movie(mock_lookup_series, mock_lookup_movie, media_manager):
    mock_lookup_movie.return_value = [{"title": "Movie A"}, {"title": "Movie B"}, {"title": "Movie C"}, {"title": "Movie D"}, {"title": "Movie E"}, {"title": "Movie F"}]

    req = MediaRequest(title="Movie", media_type="movie", is_season_pack=False, episodes=[], preferred_audio=[], resolution="1080p")
    results = await media_manager.search_media(req)

    assert len(results) == 5
    assert results[0]["_type"] == "movie"
    mock_lookup_series.assert_not_called()

@pytest.mark.asyncio
@patch.object(SonarrClient, 'lookup_series')
@patch.object(RadarrClient, 'lookup_movie')
async def test_media_manager_search_media_series(mock_lookup_movie, mock_lookup_series, media_manager):
    mock_lookup_series.return_value = [{"title": "Series A"}]

    req = MediaRequest(title="Series", media_type="series", is_season_pack=False, episodes=[], preferred_audio=[], resolution="1080p")
    results = await media_manager.search_media(req)

    assert len(results) == 1
    assert results[0]["_type"] == "series"
    mock_lookup_movie.assert_not_called()

@pytest.mark.asyncio
@patch.object(SonarrClient, 'add_series')
@patch.object(RadarrClient, 'add_movie')
async def test_media_manager_dispatch_request_movie(mock_add_movie, mock_add_series, media_manager):
    mock_add_movie.return_value = {"success": True}

    result = await media_manager.dispatch_request("movie", {"title": "Inception"})

    assert result == {"success": True}
    mock_add_movie.assert_called_once()
    mock_add_series.assert_not_called()

@pytest.mark.asyncio
@patch.object(SonarrClient, 'add_series')
@patch.object(RadarrClient, 'add_movie')
async def test_media_manager_dispatch_request_series(mock_add_movie, mock_add_series, media_manager):
    mock_add_series.return_value = {"success": True}

    result = await media_manager.dispatch_request("series", {"title": "Breaking Bad"}, season=1)

    assert result == {"success": True}
    mock_add_series.assert_called_once()
    mock_add_movie.assert_not_called()
