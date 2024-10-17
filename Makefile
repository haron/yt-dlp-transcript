build: clean
	mkdir -p src/yt_dlp_transcript && cp yt-dlp-transcript.py src/yt_dlp_transcript/__init__.py
	uv venv -q
	uv sync
	uv build

clean:
	rm -rf .python-version dist *.egg* .venv *.lock src yt_dlp_transcript-*

publish: build
	UV_PUBLISH_TOKEN=$$(cat .pypi_token) uv publish

githooks:
	git config --local core.hooksPath .githooks

linter: githooks
	uv tool run black --line-length 120 *.py
	uv tool run flake8 --config ~/.flake8 *.py

safety:
	uv tool run safety check -o bare
