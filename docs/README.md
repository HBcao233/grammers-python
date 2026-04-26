$ cd docs

# Install requirements
$ uv run --no-sync pip install -r requirements.txt

Summon html
$ uv run --no-sync python -m sphinx-build -b html source build/html

Summon gettext
$ uv run --no-sync sphinx-build -b gettext source build/gettext

Summon .po 
$ uv run --no-sync sphinx-intl update -p build/gettext -l zh-cn

Summon zh version html
$ uv run --no-sync sphinx-build -b html source build/html/zh_CN -D language='zh_CN'
