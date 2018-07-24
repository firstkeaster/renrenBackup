# coding: utf8 

from crawl import status as crawl_status
from crawl import gossip as crawl_gossip
from crawl import album as crawl_album
from crawl.utils import get_image
from config import config

from models import database, User, Comment, Like, Status, Album, Photo, Gossip

with database:
    database.create_tables([User, Comment, Like, Status, Album, Photo, Gossip])
    # status_count = crawl_status.get_status()
    gossip_count = crawl_gossip.get_gossip()

    # album_count = crawl_album.get_albums()
