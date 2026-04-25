Summon html
$ make html

Summon gettext
$ make gettext

Summon .po 
$ sphinx-intl update -p build/gettext -l zh

Summon zh version html
$ sphinx-build -b html source build/html/zh -D language='zh'
