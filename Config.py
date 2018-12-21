#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-12-18
# @Author  : InkMan
# @github  : https://github.com/BiShengOpen


# Todo: 此处用自己的API Key
API_KEY = '8gUnVP8IrVWzH62T'
# Todo: 此处用自己的Secret Key
SECRET_KEY = '37bdaef95dd4f4094076b83637dad703c844948fbd8d7a4682fb733b5a53d874'

# API请求地址
BISHENG_URL = 'http://test164.yibeix.com'
# BISHENG_URL ='https://openapi.bisheng.top'
HOST = 'test164.yibeix.com'
# 网关名称
GATEWAY = 'test1'

# 行情
TIKER_URL = '/market'
# 用户持仓
BALANCE_URL = '/account/balance'
# 用户订单记录
ORDER_LIST_URL = '/orders/list'
# 创建订单
ORDER_CREATE_URL = '/orders/create'
# 撤单
ORDER_CANCEL_URL = '/orders/cancel'
#查询订单详情
ORDER_STATUS_URL = '/orders/status'
#查询所有待成交和部分成交的订单
ORDER_UNDEAL_URL = '/orders/undeal/status'
#成交回报
RECORD_LIST_URL = '/records/list'
#获取最大的成交编号
RECORD_MAXTRDNUM_URL = '/records/maxtrdnum'
#查询成交记录(根据成交编号查询)
RECORD_TRDNUM_URL = '/records/trdnum'
#查询成交记录(根据订单编号)
RECORD_ORDNUM_URL = '/records/ordnum'
#批量查询
BATCH_QUERY_URL = '/orders/batch/status'
#批量撤单
BATCH_CANCEL_URL = '/orders/batch/cancel'
#批量下单
BATCH_CREATE_URL = '/orders/batch/create'

