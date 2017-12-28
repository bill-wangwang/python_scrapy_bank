# -*- coding: utf-8 -*-
import scrapy
from ..items import AreaItem
import json
import pymysql


class GetCitySpider(scrapy.Spider):
    # 获取城市 如 深圳 广州  玉林 北海
    name = 'get_city'

    # start_urls = ['http://m.ccb.com/mobile/branch/selectAreaOp.gsp']

    # prov:440

    def start_requests(self):
        db = pymysql.connect("127.0.0.1", "root", "123456", "bank", charset="utf8")
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select id from bank_area where fid='' "
        cur.execute(sql)
        href_list = cur.fetchall()
        url = "http://m.ccb.com/mobile/branch/selectAreaOp.gsp"
        for one in href_list:
            yield scrapy.FormRequest(
                url=url,
                formdata={"prov": one["id"]},
                meta={"prov": one["id"]}
            )

    def parse(self, response):
        print("获取网页成功，即将分析入库。。。。。。")
        item = AreaItem()
        meta = response.request.meta
        fid = meta['prov']
        data = response.text
        list = json.loads(data)
        for area in list:
            item['id'] = area["code"]
            item['name'] = area["name"]
            item['fid'] = fid
            yield item
        print("数据分析完毕。。。。。。")
    pass
