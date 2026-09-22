import os
import sys
import pytest
from unittest.mock import AsyncMock, patch, MagicMock

# Ensure parent directory is in python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from media_clients import RadarrClient

@pytest.mark.asyncio
@patch("media_clients.httpx.AsyncClient")
async def test_lookup_movie_success(mock_async_client):
    mock_client_instance = AsyncMock()
    mock_async_client.return_value.__aenter__.return_value = mock_client_instance

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"title": "The Matrix", "year": 1999}]
    mock_client_instance.get.return_value = mock_response

    client = RadarrClient(base_url="http://test-radarr", api_key="test-key")
    result = await client.lookup_movie("Matrix")

    assert result == [{"title": "The Matrix", "year": 1999}]
    mock_client_instance.get.assert_called_once_with(
        "http://test-radarr/api/v3/movie/lookup",
        params={"term": "Matrix"},
        headers={"X-Api-Key": "test-key"}
    )

@pytest.mark.asyncio
@patch("media_clients.httpx.AsyncClient")
async def test_lookup_movie_non_200(mock_async_client):
    mock_client_instance = AsyncMock()
    mock_async_client.return_value.__aenter__.return_value = mock_client_instance

    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_client_instance.get.return_value = mock_response

    client = RadarrClient(base_url="http://test-radarr", api_key="test-key")
    result = await client.lookup_movie("Matrix")

    assert result == []
    mock_client_instance.get.assert_called_once_with(
        "http://test-radarr/api/v3/movie/lookup",
        params={"term": "Matrix"},
        headers={"X-Api-Key": "test-key"}
    )
