# 使用说明
- 该爬虫为2017年最新的银行联行号数据（这是本人学python以来第2次完成的练手项目，要求别太高^_^）
- 环境要求 python3 + scrapy1.4 + redis5.6
- 使用步骤
    - 导入下面的sql语句(注意host为localhost user为root 密码为123456)
    - 进入工作目录（cd到与scrapy.cfg所在的目录）
    - scrapy crawl 1_get_bank_type
    - scrapy crawl 2_get_city
    - scrapy crawl 3_get_prov
    - scrapy crawl 4_get_bank
    - settings.py 中的 ITEM_PIPELINES （需要做相应的修改，顺序位一一对应）   
            ITEM_PIPELINES = {    
                'bank.pipelines.BankTypePipeline': 1,    
                # 'bank.pipelines.AreaPipeline': 2,   
                # 'bank.pipelines.AreaPipeline': 3,   
                # 'bank.pipelines.BankPipeline': 4,  
            }  
    - 以上命令必须按顺序一个个执行，并且等前一个执行完成才可以执行后面的



# 建库建表sql
```
CREATE DATABASE IF NOT EXISTS `bank` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `bank`;

CREATE TABLE IF NOT EXISTS `bank_area` (
  `id` char(10) NOT NULL COMMENT '省份（城市）编号',
  `fid` char(10) DEFAULT '' COMMENT '为空时表示省份，否则代表省份编号',
  `name` char(50) DEFAULT '' COMMENT '省份（城市）名称',
  PRIMARY KEY (`id`),
  KEY `fid` (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行省份地区表';

CREATE TABLE IF NOT EXISTS `bank_bank` (
  `orga_name` char(50) NOT NULL COMMENT '银行名称',
  `paym_numb` char(12) NOT NULL COMMENT '12位联行号（3位银行类型编号 + 4位地区 + 3 位银行编号 + 1位校验码）',
  `bank_type_id` char(3) NOT NULL COMMENT '3位银行类型编号',
  `prov_id` char(3) NOT NULL COMMENT '3位省份编号',
  `city_id` char(4) NOT NULL COMMENT '4位地区号',
  PRIMARY KEY (`paym_numb`),
  KEY `bank_id` (`bank_type_id`),
  KEY `city_id` (`city_id`),
  KEY `prov_id` (`prov_id`),
  KEY `orga_name` (`orga_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行联行号表';

CREATE TABLE IF NOT EXISTS `bank_bank_type` (
  `id` char(3) NOT NULL COMMENT '3位银行编码',
  `name` char(50) DEFAULT NULL COMMENT '银行分类名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行类型表';

```
温馨提示： **/out/bank_data.sql** 为采集好的数据，可以直接用
# 注意事项
- 一共有4个爬虫，
- **1_get_bank_type** 银行类型爬虫
- **2_get_city** 省份爬虫
- **3_get_prov** 城市爬虫
- **4_get_bank** 银行爬虫
 
crawl **1_get_bank_type** **2_get_city** **3_get_prov** **4_get_bank** 时的setting如下
```
#1_get_bank_type
ITEM_PIPELINES = {    
    'bank.pipelines.BankTypePipeline': 1,    
    # 'bank.pipelines.AreaPipeline': 2,   
    # 'bank.pipelines.AreaPipeline': 3,   
    # 'bank.pipelines.BankPipeline': 4,  
} 

#2_get_city
ITEM_PIPELINES = {    
    # 'bank.pipelines.BankTypePipeline': 1,    
    'bank.pipelines.AreaPipeline': 2,   
    # 'bank.pipelines.AreaPipeline': 3,   
    # 'bank.pipelines.BankPipeline': 4,  
} 

#3_get_prov
ITEM_PIPELINES = {    
    # 'bank.pipelines.BankTypePipeline': 1,    
    # 'bank.pipelines.AreaPipeline': 2,   
    'bank.pipelines.AreaPipeline': 3,   
    # 'bank.pipelines.BankPipeline': 4,  
} 

#4_get_bank
ITEM_PIPELINES = {    
    # 'bank.pipelines.BankTypePipeline': 1,    
    # 'bank.pipelines.AreaPipeline': 2,   
    # 'bank.pipelines.AreaPipeline': 3,   
    'bank.pipelines.BankPipeline': 4,  
} 
```
