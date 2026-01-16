pip uninstall -y grammers
pip install target/wheels/$(ls -t target/wheels/ | head -n 1)
pytest