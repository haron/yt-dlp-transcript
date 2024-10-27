#!/usr/bin/env python

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory

import srt
from configargparse import ArgumentDefaultsRawHelpFormatter, ArgumentParser
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError  # noqa

default_opts = {
    "no_warnings": True,
    "noprogress": True,
    "postprocessors": [
        {"format": "srt", "key": "FFmpegSubtitlesConvertor", "when": "before_dl"},
    ],
    "quiet": True,
    "retries": 10,
    "skip_download": True,
    "writeautomaticsub": True,
}


def yt_dlp_transcript(url=None, language="en", verbose=False, **kwargs):
    with TemporaryDirectory() as temp_dir:
        path = Path(temp_dir)
        opts = deepcopy(default_opts)
        opts["outtmpl"] = {"default": str(path / "res")}
        opts["subtitleslangs"] = [language]
        opts.update(kwargs)
        if verbose:
            del opts["quiet"]
            print(opts)
        ydl = YoutubeDL(opts)
        ydl.download(url)
        srt_files = list(path.glob("*"))
        if len(srt_files) < 1:
            raise DownloadError(f"Error: cannot download subtitles for {url}, probably the video has no subtitles.")
        subtitles = srt.parse(open(srt_files[0]).read())
        res = " ".join([s.content.replace(r"\h", "") for s in subtitles])
        return res


def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsRawHelpFormatter)
    parser.add_argument("-l", "--language", default="en", help="subtitles language")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    parser.add_argument("url", help="Youtube URL")
    args = parser.parse_args()
    print(yt_dlp_transcript(**args.__dict__))


if __name__ == "__main__":
    main()
