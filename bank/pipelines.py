# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import logging


class BankTypePipeline(object):
    def __init__(self):
        self.db = None
        self.cur = None

    def open_spider(self, spider):
        self.db = pymysql.connect("127.0.0.1", "root", "123456", "bank", charset="utf8")
        self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        insert_sql = "insert into bank_bank_type (`id`, `name` ) " \
                     "values('{}', '{}')". \
            format(item['id'], item['name'])
        print(insert_sql)
        try:
            self.cur.execute(insert_sql)
            self.db.commit()
        except:
            print("*" * 110)
            print("sql语句【{}】执行失败".format(insert_sql))
            logging.error("插入银行分类表失败(sql={})".format(insert_sql))
            print("*" * 110)
            self.db.rollback()
        return item

    def spider_close(self, spider):
        self.db.close()


class AreaPipeline(object):
    def __init__(self):
        self.db = None
        self.cur = None

    def open_spider(self, spider):
        self.db = pymysql.connect("127.0.0.1", "root", "123456", "bank", charset="utf8")
        self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        insert_sql = "insert into bank_area (`id`, `name`, `fid` ) " \
                     "values('{}', '{}', '{}' )". \
            format(item['id'], item['name'], item['fid'])
        print("-" * 100)
        print(insert_sql)
        try:
            self.cur.execute(insert_sql)
            self.db.commit()
        except:
            print("*" * 110)
            print("sql语句【{}】执行失败".format(insert_sql))
            logging.error("插入省份地区表失败(sql={})".format(insert_sql))
            print("*" * 110)
            self.db.rollback()
        return item

    def spider_close(self, spider):
        self.db.close()


class BankPipeline(object):
    def __init__(self):
        self.db = None
        self.cur = None

    def open_spider(self, spider):
        self.db = pymysql.connect("127.0.0.1", "root", "123456", "bank", charset="utf8")
        self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        insert_sql = "insert into bank_bank (`orga_name`, `paym_numb`, `bank_type_id`, `prov_id`, `city_id` ) " \
                     "values('{}', '{}', '{}', '{}', '{}' )". \
            format(item['orga_name'], item['paym_numb'], item['bank_type_id'], item['prov_id'], item['city_id'])
        try:
            self.cur.execute(insert_sql)
            self.db.commit()
        except:
            logging.error("插入银行表失败(sql={})".format(insert_sql))
            print("插入银行表失败(sql={})".format(insert_sql))
            self.db.rollback()
        return item

    def spider_close(self, spider):
        self.db.close()
