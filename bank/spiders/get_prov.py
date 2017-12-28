# -*- coding: utf-8 -*-
import scrapy
from ..items import AreaItem


class GetProvSpider(scrapy.Spider):
    # 获取省份 如 广东 广西 湖南 湖北
    name = 'get_prov'
    start_urls = ['http://m.ccb.com/jsp/ccbcom/mobile/branch/mobileBpSelectOp.gsp']

    def parse(self, response):
        item = AreaItem()
        print("获取网页成功，即将分析入库。。。。。。")
        bank_list = response.xpath("//select[@name='AreaProv']/option")
        for bank in bank_list:
            value = bank.xpath("./@value").extract()[0]
            name = bank.xpath("./text()").extract()[0]
            if value != "":
                item['id'] = value
                item['name'] = name
                item['fid'] = ""
                yield item
            else:
                print("value 是空的 。。。。")
        print("数据分析完毕。。。。。。")
    pass
