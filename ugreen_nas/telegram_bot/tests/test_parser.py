"""
Unit tests for Natural Language Media Parser.
Validates intent extraction, typo correction, resolution mapping, and audio preferences.
"""
import os
import sys
import pytest

# Ensure parent directory is in python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_parser import parse_with_heuristics, MediaRequest


def test_parse_movie_simple():
    req = parse_with_heuristics("Download Inception in 1080p")
    assert req.title == "Inception"
    assert req.media_type == "movie"
    assert req.resolution == "1080p"
    assert "Hindi" in req.preferred_audio


def test_parse_movie_4k_hindi():
    req = parse_with_heuristics("Get Interstellar in 4k with Hindi audio")
    assert req.title == "Interstellar"
    assert req.resolution == "4K"
    assert req.preferred_audio[0] == "Hindi"


def test_parse_series_season_pack():
    req = parse_with_heuristics("Download Stranger Things Season 4 in 1080p")
    assert "Stranger Things" in req.title
    assert req.media_type == "series"
    assert req.season == 4
    assert req.is_season_pack is True
    assert req.resolution == "1080p"


def test_parse_series_episode_range():
    req = parse_with_heuristics("Fetch Breaking Bad season 1 episodes 1 to 4 in 1080p")
    assert "Breaking Bad" in req.title
    assert req.media_type == "series"
    assert req.season == 1
    assert req.episodes == [1, 2, 3, 4]
    assert req.is_season_pack is False


def test_parse_typo_correction():
    req = parse_with_heuristics("stranger thing s4")
    assert req.title == "Stranger Things"
    assert req.media_type == "series"
    assert req.season == 4


def test_parse_subtitles_default():
    req = parse_with_heuristics("House of the Dragon in 4K")
    assert req.title == "House of the Dragon"
    assert req.resolution == "4K"
    assert req.embedded_subtitles is True
