#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os

logging.basicConfig(filename = os.path.join(os.getcwd(), 'debug.log'), level=logging.DEBUG, filemode='w',
                    format='%(asctime)s - %(levelname)s: %(message)s')

log = logging.getLogger('root')