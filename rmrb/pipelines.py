# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

class RmrbPipeline(object):
    def process_item(self, item, spider):
        return item

class CleaningPipeline(object):
    """Remove image tag and JavaScript code from HTML source."""

    def process_item(self, item, spider):
        text = re.sub(r'<img [\s\S]*?>', '', item['text'])
        text = re.sub(r'<script[\s\S]*?>[\s\S]+?</script>', '', text)
        text = re.sub(r'<style[\s\S]*?>[\s\S]+?</style>', '', text)
        text = re.sub(r'<a [\s\S]*?>[\s\S]+?</a>', '', text)
        text = re.sub(r'<[\s\S]*>\S*?</\s+?>', '', text)
        text = re.sub(r'<p><br></p>', '', text)
        text = re.sub(r'<p><mpvoice[\s\S]+?</p>', '', text)
        text = re.sub(r'height: 100%', '', text)
        text = re.sub(r'<p style="white-space: normal;max-width: 100%;min-height: 1em;letter-spacing: 0.544px;line-height: 25.6px;text-align: right;box-sizing: border-box !important;overflow-wrap: break-word !important;">[\s\S]+?</p>', '', text)
        text = re.sub(r'\s*\n+', '\n', text)
        text = re.sub(r'\n+', '\n', text)

        item['text'] = text

        return item
