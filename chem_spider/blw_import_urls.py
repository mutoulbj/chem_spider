#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mongodb import db


def import_urls(file):
    with open(file, 'r') as f:
        while True:
            line = f.readline().strip()

            if not line:
                break

            # db.blw_urls.update({'url': line}, {'url': line}, upsert=True)
            db.blw_urls.insert({'url': line})


if __name__ == '__main__':
    import_urls('blw.txt')