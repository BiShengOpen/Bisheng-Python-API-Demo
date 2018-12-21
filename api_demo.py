#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-12-18
# @Author  : InkMan
# @github  : https://github.com/BiShengOpen

from pprint import pprint
from Services import *

if __name__ == '__main__':
    print(u' 获取资产信息 ')
    holding = query_hld(prd_names="ETH_USDT")
    pprint(holding['data'])

    print(u' 获取行情信息 ')
    tiker = mkt_query(mkt="ETH_USDT")
    pprint(tiker['data'])

    # 获取买一和卖一
    data = tiker['data']
    buy1 = 0
    sell1 = 0
    if 0 != len(data['sell']):
        sell1 = data['sell'][0]['ordPrice']
    if 0 != len(data['buy']):
        buy1 = data['buy'][0]['ordPrice']
    pprint('buy1:{0},sell1:{1}'.format(buy1, sell1))
    buy_price = round(buy1 + 0.0001, 4)
    sell_price = round(sell1 - 0.0001, 4)
    pprint('buy_price:{:f},sell_price:{:f}'.format(buy_price, sell_price))

    print(u' 挂单 ')
    # order_create(random.choice(('B', 'S')), mkt, str(round(random.uniform(0, 1), 4)), str(round(random.uniform(1, 10), 2)))
    order_info = order_create(side='B', mkt='ETH_USDT', price='{:f}'.format(buy_price), qty='10')
    pprint(order_info['data'])

    print(u' 查询订单状态 ')
    order_status = query_ord_status(order_info['data']['ordNum'])
    pprint(order_status['data'])

    print(u' 撤单 ')
    order_cancel_info = order_cancel(order_info['data']['ordNum'])
    pprint(order_cancel_info['data'])

    # print(u' 查询所有未成交订单 ')
    # order_undeal = query_undeal_order(1,10)
    # pprint(order_undeal['data'])
    # 撤单
    # for item in order_undeal['data']:
    #     order_cancel_info = order_cancel(item['ordNum'])
    #     pprint(order_cancel_info['data'])
