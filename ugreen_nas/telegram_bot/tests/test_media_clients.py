import os
import sys
import pytest
from unittest.mock import AsyncMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from media_clients import MediaManager
from llm_parser import MediaRequest

@pytest.fixture
def mock_sonarr():
    return AsyncMock()

@pytest.fixture
def mock_radarr():
    return AsyncMock()

@pytest.fixture
def media_manager(mock_sonarr, mock_radarr):
    manager = MediaManager()
    manager.sonarr.lookup_series = mock_sonarr
    manager.radarr.lookup_movie = mock_radarr
    return manager

@pytest.mark.asyncio
async def test_search_media_series_only(media_manager, mock_sonarr, mock_radarr):
    req = MediaRequest(title="Breaking Bad", media_type="series")
    mock_sonarr.return_value = [{"title": "Breaking Bad", "year": 2008}]

    results = await media_manager.search_media(req)

    assert len(results) == 1
    assert results[0]["_type"] == "series"
    assert results[0]["title"] == "Breaking Bad"

    mock_sonarr.assert_called_once_with("Breaking Bad")
    mock_radarr.assert_not_called()

@pytest.mark.asyncio
async def test_search_media_movie_only(media_manager, mock_sonarr, mock_radarr):
    req = MediaRequest(title="Inception", media_type="movie")
    mock_radarr.return_value = [{"title": "Inception", "year": 2010}]

    results = await media_manager.search_media(req)

    assert len(results) == 1
    assert results[0]["_type"] == "movie"
    assert results[0]["title"] == "Inception"

    mock_sonarr.assert_not_called()
    mock_radarr.assert_called_once_with("Inception")

@pytest.mark.asyncio
async def test_search_media_unknown_both(media_manager, mock_sonarr, mock_radarr):
    req = MediaRequest(title="Matrix", media_type="unknown")
    mock_sonarr.return_value = [{"title": "Matrix (Series)", "year": 2020}]
    mock_radarr.return_value = [{"title": "The Matrix", "year": 1999}]

    results = await media_manager.search_media(req)

    assert len(results) == 2
    assert results[0]["_type"] == "series"
    assert results[1]["_type"] == "movie"

    mock_sonarr.assert_called_once_with("Matrix")
    mock_radarr.assert_called_once_with("Matrix")

@pytest.mark.asyncio
async def test_search_media_unknown_cap(media_manager, mock_sonarr, mock_radarr):
    req = MediaRequest(title="Star", media_type="unknown")
    # Return 5 series
    mock_sonarr.return_value = [{"title": f"Star Series {i}"} for i in range(5)]
    mock_radarr.return_value = [{"title": "Star Movie"}]

    results = await media_manager.search_media(req)

    # Results should be capped at 5 from Sonarr, Radarr shouldn't be called because len(results) >= 5
    assert len(results) == 5
    for r in results:
        assert r["_type"] == "series"

    mock_sonarr.assert_called_once_with("Star")
    mock_radarr.assert_not_called()

@pytest.mark.asyncio
async def test_search_media_combined_cap(media_manager, mock_sonarr, mock_radarr):
    req = MediaRequest(title="Test", media_type="unknown")
    # Return 3 series and 4 movies (total 7)
    mock_sonarr.return_value = [{"title": f"Series {i}"} for i in range(3)]
    mock_radarr.return_value = [{"title": f"Movie {i}"} for i in range(4)]

    results = await media_manager.search_media(req)

    # Results should be capped at 5 total
    assert len(results) == 5
    # First 3 are series
    assert results[0]["_type"] == "series"
    assert results[2]["_type"] == "series"
    # Next 2 are movies
    assert results[3]["_type"] == "movie"
    assert results[4]["_type"] == "movie"

    mock_sonarr.assert_called_once_with("Test")
    mock_radarr.assert_called_once_with("Test")
