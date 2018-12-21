#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-12-18
# @Author  : InkMan
# @github  : https://github.com/BiShengOpen

from Utils import *
from Config import *


# 批量查询
def order_batch_query(ords):
    params = {}
    if ords:
        params['ords'] = ords
    return api_key_post(params, BATCH_QUERY_URL)


# 批量撤单
def order_batch_cancel(ords):
    params = {}
    if ords:
        params['ords'] = ords
    return api_key_post(params, BATCH_CANCEL_URL)


# 批量下单
def order_batch_create(ords):
    params = {}
    if ords:
        params['ords'] = ords
    return api_key_post(params, BATCH_CREATE_URL)


# 挂单
def order_create(side, mkt, price, qty):
    """
    :param side: 订单类型，B/买单，S/卖单
    :param mkt: BSH_ETH/指定市场
    :param price: 对价,以计价货币(BTC、ETH、USDT、WIT等)为计价单位的价格，最多支持8位小数，多于8位直接舍去
    :param qty:交易产品数量,1表示一个BTC或ETH,最多支持八位小数
    :param type:订单类型, M: 市价，L: 限价,目前只支持限价L
    :return:
    """
    params = {'side': side,
              'mkt': mkt,
              'price': price,
              'qty': qty,
              'type': 'L'}
    return api_key_post(params, ORDER_CREATE_URL)


# 撤单
def order_cancel(ord_num):
    params = {'ordNum': ord_num}
    return api_key_post(params, ORDER_CANCEL_URL)


# 成交回报查询
def trd_query(mkt, page_num, page_size, start_time, end_time):
    params = {'mkt': mkt,
              'pageNum': page_num,
              'pageSize': page_size,
              'startTime': start_time,
              'endTime': end_time}
    return api_key_get(params, RECORD_LIST_URL)


# 最大的成交编号查询
def query_max_trd_num():
    params = {}
    return api_key_get(params, RECORD_MAXTRDNUM_URL)


# 查询成交记录
def query_trd_num(start_num, end_num):
    params = {'startNum': start_num,
              'endNum': end_num}
    return api_key_get(params, RECORD_TRDNUM_URL)


# 查询成交记录(订单编号)
def query_trd_ord_num(ord_num):
    params = {'ordNum': ord_num}
    return api_key_post(params, RECORD_ORDNUM_URL)


# 查询订单状态(订单编号)
def query_ord_status(ord_num):
    params = {'ordNum': ord_num}
    return api_key_get(params, ORDER_STATUS_URL)


# 查询未成交订单
def query_undeal_order(page_num, page_size):
    params = {'pageNum': page_num,
              'pageSize': page_size}
    return api_key_get(params, ORDER_UNDEAL_URL)


# 行情查询
def mkt_query(mkt):
    params = {'mkt': mkt}
    return api_key_get(params, TIKER_URL)


# 下单历史查询
def query_ord_list(type, mkt, page_num, page_size, start_time, end_time):
    params = {'type': type,
              'mkt': mkt,
              'pageNum': page_num,
              'pageSize': page_size,
              'startTime': start_time,
              'endTime': end_time}
    return api_key_get(params, ORDER_LIST_URL)


#资产查询
def query_hld(prd_names):
    params = {'prdNames': prd_names}
    return api_key_get(params, BALANCE_URL)
