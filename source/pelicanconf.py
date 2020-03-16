#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kostyrko'
SITENAME = 'Code Snippets'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/m_kostyrko'),
         ('Github', 'https://github.com/kostyrko'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# set output folder
OUTPUT_PATH = '../output'

# set theme folder
THEME = 'theme'

# set plugin folder
PLUGIN_PATHS = ['plugins/', ]

# set plugins
PLUGINS = ['i18n_subsites', ]

# add jinja envir. for i18n_subsite
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# setting bootstrap theme
# from source/theme/css
BOOTSTRAP_THEME = 'flatly'

# setting Pygments code highlighter
# from source/theme/css/pygments
PYGMENTS_STYLE = 'monokai'

# set path for articles/blog posts     
ARTICLE_PATHS = ['articles']

# set static media files path
STATIC_PATHS = ['img', 'pdf']

# set pages folder link
PAGE_PATHS = ['pages']

# set custom url
# add date
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# set pages url
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# set category url
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# set tag url
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'