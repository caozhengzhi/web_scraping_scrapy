# -*- coding: utf-8 -*-
BOT_NAME = 'wiki'

SPIDER_MODULES = ['wiki.spiders']
NEWSPIDER_MODULE = 'wiki.spiders'

DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {'wiki.pipelines.WikiPipeline': 100, }