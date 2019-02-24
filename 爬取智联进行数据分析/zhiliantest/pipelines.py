# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
class ZhiliantestPipeline(object):
    def process_item(self, item, spider):
        welfare = ','.join(item['welfare'])
        item['welfare'] =welfare
        return item


from openpyxl import Workbook


class ExcelPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['职位', '薪资', '学历', '是否全职','工作年限', '地址', '公司名称','公司类型','公司人数', '待遇', '发布时间', 'url'])

    def process_item(self, item, spider):
        line = [item['jobName'],item['salary'],item['eduLevel'],item['emplType'],item['workingExp'],item['city_display'],item['company'],item['company_type'],item['company_size'],item['welfare'],item['updateDate'],item['url']]
        self.ws.append(line)
        self.wb.save('数据12.xlsx')
        return item





