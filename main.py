############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import environ
import sys
import os
import django

sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

env = environ.Env()
environ.Env.read_env()

django.setup()

# Import your models for use in your script
from db.models import *
from db._article_list_parser import parse_article_list
from db._feeds_parser import parse_feeds
from db._article_parser import parse_articles
from db._tagger import do_tagger
from db._shows_parser import parse_shows

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few users in the database
parse_article_list()
print("parse_article_list done")
# parse_feeds()
# print("parse_feeds done")
# parse_articles()
# print("parse_articles done")
# do_tagger()
# print("do_tagger done")
# parse_shows()
# print("parse_shows done")