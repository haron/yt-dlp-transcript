# yt-dlp-transcript

A handy wrapper for `yt-dlp` to download transcripts for YouTube videos.

## Usage

    uvx yt-dlp-transcript https://www.youtube.com/watch?v=dQw4w9WgXcQ

or:

    pip install yt-dlp-transcript
    yt-dlp-transcript https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Options:

    > yt-dlp-transcript -h
    usage: yt-dlp-transcript [-h] [-l LANGUAGE] [-v] url

    positional arguments:
      url                   Youtube URL

    options:
      -h, --help            show this help message and exit
      -l LANGUAGE, --language LANGUAGE
                            subtitles language (default: en)
      -v, --verbose         verbose mode (default: False)

## Usage in Python code

    from yt_dlp_transcript import yt_dlp_transcript
    print(yt_dlp_transcript("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
