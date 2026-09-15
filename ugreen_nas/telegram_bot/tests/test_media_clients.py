import os
import sys
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
import httpx

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from media_clients import RadarrClient

@pytest.mark.asyncio
async def test_radarr_lookup_movie_missing_title():
    client = RadarrClient(base_url="http://fake", api_key="fake")

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = [{"year": 2020}, {"title": "Valid Movie", "year": 2021}] # Missing title for one item

    with patch('httpx.AsyncClient.get', new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_resp

        res = await client.lookup_movie("test")
        assert len(res) == 1
        assert res[0]["title"] == "Valid Movie"

@pytest.mark.asyncio
async def test_radarr_lookup_movie_invalid_json():
    client = RadarrClient(base_url="http://fake", api_key="fake")

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.side_effect = ValueError("Invalid JSON")

    with patch('httpx.AsyncClient.get', new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_resp

        res = await client.lookup_movie("test")
        assert res == []
