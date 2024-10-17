from yt_dlp import YoutubeDL
from tempfile import TemporaryDirectory
from pathlib import Path
from configargparse import ArgumentParser, ArgumentDefaultsRawHelpFormatter
import srt

opts = {
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


def download(args):
    with TemporaryDirectory() as temp_dir:
        path = Path(temp_dir)
        opts["outtmpl"] = {"default": str(path / "res")}
        opts["subtitleslangs"] = [args.language]
        if args.verbose:
            print(opts)
        ydl = YoutubeDL(opts)
        ydl.download(args.url)
        srt_file = list(path.glob("*"))[0]
        subtitles = srt.parse(open(srt_file).read())
        res = " ".join([s.content.replace(r"\h", "") for s in subtitles])
        return res


def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsRawHelpFormatter)
    parser.add_argument("-l", "--language", default="en", help="subtitles language")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    parser.add_argument("url", help="Youtube URL")
    args = parser.parse_args()
    print(download(args))


if __name__ == "__main__":
    main()
