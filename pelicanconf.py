#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os


AUTHOR = u'3 Strand Code'
SITENAME = u'3 Strand Code Blog'
SITEURL = "http://127.0.0.1:8080"
#SITEURL = os.environ.get("PELICAN_SITEURL")
#assert SITEURL, "Missing PELICAN_SITEURL environment variable (URL path before static files)"

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

THEME = 'themes/Casper2Pelican'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('3 Strand Code Home', 'http://3strandcode.com/'),
    ('Dev-Coop Code Repository', 'http://github.com/dev-coop/'),
)

# Social widget
SOCIAL = (
    ('Dev-Coop meetup', 'http://www.meetup.com/dev-coop/'),
)

DEFAULT_PAGINATION = 5

DISQUS_SITENAME = "3strandcode"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
