dev: 
	maturin develop

build: 
	maturin build --release

test-dependencies:
	uv pip install pytest pytest-asyncio

test: test-dependencies
	uv run --no-sync pytest --log-cli-level=WARNING