#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alexander Teleshov'
SITENAME = u'HallEffect\'s notes'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

LOCALE = 'ru_RU.UTF-8'
DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# путь к исходникам
PATH = 'content'
# путь к выходным html-файлам
# в целом настройка не важна,
# ибо генерировать всё, кроме постов
# будем в корень проекта
OUTPUT_PATH = 'articles/'
# как сохранять посты
ARTICLE_URL = 'articles/{slug}/'
# куда сохранять посты
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "halleffect"

THEME = "/home/akela/halleffect.github.io/.env/lib/python2.7/site-packages/pelican/themes/pelican-bootstrap3"

PYGMENTS_STYLE = "monokai"

SHOW_ARTICLE_CATEGORY= True
SHOW_DATE_MODIFIED = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

#BOOTSTRAP_NAVBAR_INVERSE = False
#DISPLAY_PAGES_ON_MENU=True
# HIDE_SIDEBAR = True

BOOTSTRAP_THEME = "flatly"

USE_OPEN_GRAPH = True