pip uninstall -y grammers
target=target
if [[ -n "$CARGO_TARGET_DIR" ]]; then
    target=$CARGO_TARGET_DIR
fi
pip install $target/wheels/$(ls -t $target/wheels/ | head -n 1)
pytest --log-cli-level=INFO