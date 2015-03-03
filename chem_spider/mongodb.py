#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo

from settings import mongodb_uri, mongodb_db_name, mongodb_user, mongodb_passwd

conn = pymongo.MongoClient(mongodb_uri)
db = conn[mongodb_db_name]
db.authenticate(mongodb_user, mongodb_passwd)