.PHONY: test

build: clean linter
	mkdir -p src/yt_dlp_transcript && cp yt-dlp-transcript.py src/yt_dlp_transcript/__init__.py
	uv venv -q --clear
	uv sync
	uv build

clean:
	rm -rf .python-version dist *.egg* .venv *.lock src yt_dlp_transcript-*

publish: test
	UV_PUBLISH_TOKEN=$$(cat .pypi_token) uv publish

githooks:
	git config --local core.hooksPath .githooks

linter: githooks
	uv run isort -q **/*.py
	uv run ruff format -q **/*.py
	uvx ruff check

safety:
	uvx safety check -o bare

test: build
	.venv/bin/pytest
