import pytest
from yt_dlp_transcript import yt_dlp_transcript
from yt_dlp.utils import DownloadError

def test_transcript_contains_expected_text():
    """Test that transcript contains expected text from a known video."""
    url = "https://www.youtube.com/watch?v=5siqfFnLSdw"
    transcript = yt_dlp_transcript(url)
    assert "some comfort pets" in transcript.lower()

def test_invalid_url():
    """Test that invalid URL raises DownloadError."""
    with pytest.raises(DownloadError):
        yt_dlp_transcript("https://www.youtube.com/watch?v=invalid")
