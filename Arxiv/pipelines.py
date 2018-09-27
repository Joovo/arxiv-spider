# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ArxivPipeline(object):
    def __init__(self):
        self.file = open('./items.json', 'wb')

    def process_item(self, item, spider):
        content = (json.dumps(dict(item))+"\n").encode(encoding='utf-8')
        self.file.write(content)
        return item
