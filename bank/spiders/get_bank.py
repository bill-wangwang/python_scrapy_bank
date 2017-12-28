# -*- coding: utf-8 -*-
import scrapy
from ..items import AreaItem
import json
import pymysql


class GetCitySpider(scrapy.Spider):
    # 获取银行联行号  银行类型 * 省份 * 城市
    name = 'get_bank'

    # start_urls = ['http://m.ccb.com/mobile/branch/selectAreaOp.gsp']

    # prov:440

    def start_requests(self):
        url = "http://m.ccb.com/mobile/branch/selectDelhhOp.gsp"
        bank_id = 201
        prov_id = 440
        city_id = 5860
        data = {"bank": str(bank_id), "prov": str(prov_id), "area": str(city_id)}
        yield scrapy.FormRequest(
            url=url,
            formdata=data,
            meta=data
        )
        # db = pymysql.connect("127.0.0.1", "root", "123456", "bank", charset="utf8")
        # cur_bank_type = db.cursor(cursor=pymysql.cursors.DictCursor)
        # cur_prov = db.cursor(cursor=pymysql.cursors.DictCursor)
        # cur_city = db.cursor(cursor=pymysql.cursors.DictCursor)
        # sql_bank_type = "select id from bank_bank_type "
        # sql_bank_prov = "select id from bank_area where fid='' "
        # cur_bank_type.execute(sql_bank_type)
        # bank_type_list = cur_bank_type.fetchall()
        #
        # cur_prov.execute(sql_bank_prov)
        # prov_list = cur_prov.fetchall()
        # for bank_type in bank_type_list:
        #     for prov in prov_list:
        #         sql_city = "select id from bank_area where fid='{}' " . format(prov["id"])
        #         cur_city.execute(sql_city)
        #         city_list = cur_city.fetchall()
        #         for city in city_list:
        #             print(bank_type["id"] + "\t" + prov["id"] + "\t" + city["id"])

        # yield scrapy.FormRequest(
        #     url=url,
        #     formdata={"prov": one["id"]},
        #     meta={"prov": one["id"]}
        # )

    def parse(self, response):
        print("获取网页成功，即将分析入库。。。。。。")
        meta = response.request.meta
        print(meta["bank"] + "\t" + meta["prov"] + "\t" + meta["area"])
        data = response.body
        print(data)
        txt = response.text
        print(txt)

        # list = json.loads(data)
        # print(list)
        # item = AreaItem()
        # meta = response.request.meta
        # fid = meta['prov']
        # data = response.text
        # list = json.loads(data)
        # for area in list:
        #     item['id'] = area["code"]
        #     item['name'] = area["name"]
        #     item['fid'] = fid
        #     yield item
        # print("数据分析完毕。。。。。。")

    pass
