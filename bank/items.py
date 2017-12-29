# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BankTypeItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    pass


class AreaItem(scrapy.Item):
    id = scrapy.Field()
    fid = scrapy.Field()
    name = scrapy.Field()
    pass


class BankItem(scrapy.Item):
    # 'orgaName': '中国农业银行股份有限公司深圳天悦湾支行', 'paymNumb': '103584000404'
    # (meta["bank"] + "\t" + meta["prov"] + "\t" + meta["area"]
    orga_name = scrapy.Field()
    paym_numb = scrapy.Field()
    bank_type_id = scrapy.Field()
    prov_id = scrapy.Field()
    city_id = scrapy.Field()
    pass
