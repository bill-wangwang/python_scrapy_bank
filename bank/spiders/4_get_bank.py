# -*- coding: utf-8 -*-
import scrapy
from ..items import BankItem
import json
import pymysql
import logging


class GetCitySpider(scrapy.Spider):
    # 获取银行联行号  银行类型 * 省份 * 城市
    name = '4_get_bank'

    # start_urls = ['http://m.ccb.com/mobile/branch/selectAreaOp.gsp']

    # prov:440

    def start_requests(self):
        logging.error("开始采集银行信息" + "." * 80)
        url = "http://m.ccb.com/mobile/branch/selectDelhhOp.gsp"
        # bank_id = 103
        # prov_id = 440
        # city_id = 5840
        # data = {"bank": str(bank_id), "prov": str(prov_id), "area": str(city_id)}
        # yield scrapy.FormRequest(
        #     url=url,
        #     formdata=data,
        #     meta=data
        # )
        db = pymysql.connect("127.0.0.1", "root", "123456", "bank", charset="utf8")
        cur_bank_type = db.cursor(cursor=pymysql.cursors.DictCursor)
        cur_prov = db.cursor(cursor=pymysql.cursors.DictCursor)
        cur_city = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql_bank_type = "select id from bank_bank_type "
        sql_bank_prov = "select id from bank_area where fid='' "
        cur_bank_type.execute(sql_bank_type)
        bank_type_list = cur_bank_type.fetchall()
        cur_prov.execute(sql_bank_prov)
        prov_list = cur_prov.fetchall()
        for bank_type in bank_type_list:
            for prov in prov_list:
                sql_city = "select id from bank_area where fid='{}' ".format(prov["id"])
                cur_city.execute(sql_city)
                city_list = cur_city.fetchall()
                for city in city_list:
                    # print(bank_type["id"] + "\t" + prov["id"] + "\t" + city["id"])
                    data = {"bank": str(bank_type["id"]), "prov": str(prov["id"]), "area": str(city["id"])}
                    yield scrapy.FormRequest(
                        url=url,
                        formdata=data,
                        meta=data
                    )

    def parse(self, response):
        item = BankItem()
        # {'orgaName': '中国农业银行股份有限公司深圳天悦湾支行',   'paymNumb': '103584000404', 'bankCode': ''}
        print("获取网页成功，即将分析入库。。。。。。")
        meta = response.request.meta
        # print(meta["bank"] + "\t" + meta["prov"] + "\t" + meta["area"])
        param = "bank={}&prov={}&area={}".format(meta["bank"], meta["prov"], meta["area"])
        text = response.text
        bank_list = json.loads(text)
        bank_len = len(bank_list)
        if bank_len > 0:
            logging.error(param + "记录条数位----------  {}".format(bank_len))
            for bank in bank_list:
                item["orga_name"] = bank["orgaName"]
                item["paym_numb"] = bank["paymNumb"]
                item["bank_type_id"] = meta["bank"]
                item["prov_id"] = meta["prov"]
                item["city_id"] = meta["area"]
                yield item
        else:
            logging.error(param + "没有任何记录")
        print(param + " 分析完毕，共{}条记录。".format(bank_len))
    pass
