# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ProxycollectPipeline(object):
    def open_spider(self, spider):
        filename=spider.output_name
        self.file = open(filename, 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if item['proxyAddress']:
            line = item['proxyAddress']+'\n'
            self.file.write(line)
        return item
