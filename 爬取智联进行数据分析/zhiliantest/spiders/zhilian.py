# -*- coding: utf-8 -*-
import scrapy

import json
from scrapy import Request

from zhiliantest.items import ZhiliantestItem


class ZhilianSpider(scrapy.Spider):
    name = "zhilian"
    allowed_domains = ["www.zhaopin.com"]
    start_urls = ['http://www.zhaopin.com/']
    def start_requests(self):
        for i in range(40):
            url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3'.format(i*90)
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        results = result['data']['results']
        item = ZhiliantestItem()
        for items in results:

            item['jobName'] = items['jobName']
            item['salary'] = items['salary']
            item['welfare'] = items['welfare']
            item['url'] = items['positionURL']
            item['city_display'] = items['city']['display']
            item['company'] = items['company']['name']
            item['company_size'] = items['company']['size']['name']
            item['company_type'] = items['company']['type']['name']
            item['emplType'] = items['emplType']
            item['eduLevel'] = items['eduLevel']['name']
            item['updateDate'] = items['updateDate']
            item['workingExp'] = items['workingExp']['name']
            #print(jobName,salary,welfare,url,city_display,company,emplType,eduLevel,updateDate,workingExp)
            yield item

















