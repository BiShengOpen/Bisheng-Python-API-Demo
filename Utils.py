#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-12-18
# @Author  : InkMan
# @github  : https://github.com/BiShengOpen

import base64
import hashlib
import hmac
import json
import time
import urllib
import urllib.parse
import urllib.request
import requests
import coincurve
import Config
import binascii


# 处理get 请求
def http_get_request(url, params, add_to_headers=None):
    response = requests.get(url, params=params, headers=add_to_headers, timeout=3)
    try:
        if response.status_code >= 300:
            return response.text
        else:
            return response.json()
    except BaseException as e:
        print("httpGet failed, detail is:%s,%s" % (response.text, e))
        return


# 处理post请求
def http_post_request(url, params=None, add_to_headers=None):
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    if add_to_headers:
        headers.update(add_to_headers)
    # postdata = urllib.parse.urlencode(params)
    post_data = json.dumps(params)
    response = requests.post(url, data=post_data, headers=headers, timeout=3)
    try:
        if response.status_code >= 300:
            return response.text
        else:
            return response.json()
    except BaseException as e:
        print("httpGet failed, detail is:%s,%s" % (response.text, e))
        return


# 创建get 请求签名
def api_key_get(params, request_path):
    """
        :param acct_id
        :return:
    """
    method = 'GET'
    timestamp = str(int(time.time()))
    params_to_sign = {
        'SignatureMethod': 'secp256k1',
        'SignatureVersion': '1',
        'APIKey': Config.API_KEY,
        'Timestamp': timestamp
    }
    params_to_sign.update(params)
    host_name = Config.HOST
    all_request_path = "/" + Config.GATEWAY + "/" + Config.API_KEY + request_path
    params_sort = sorted(params_to_sign.items(), key=lambda d: d[0], reverse=False)
    signature = sign(params_sort, method, host_name, all_request_path, Config.SECRET_KEY)
    url = Config.BISHENG_URL + all_request_path + '?' + urllib.parse.urlencode(
        params_sort) + '&' + 'Signature=' + urllib.parse.quote(
        signature)
    return http_get_request(url, {})


# 创建post 请求签名,
def api_key_post(params, request_path):
    method = 'POST'
    timestamp = str(int(time.time()))
    params_to_sign = {
        'SignatureMethod': 'secp256k1',
        'SignatureVersion': '1',
        'APIKey': Config.API_KEY,
        'Timestamp': timestamp
    }
    host_name = Config.HOST
    all_request_path = "/" + Config.GATEWAY + "/" + Config.API_KEY + request_path
    params_sort = sorted(params_to_sign.items(), key=lambda d: d[0], reverse=False)
    signature = sign(params_sort, method, host_name, all_request_path, Config.SECRET_KEY)
    url = Config.BISHENG_URL + all_request_path + '?' + urllib.parse.urlencode(
        params_sort) + '&' + 'Signature=' + urllib.parse.quote(signature)
    return http_post_request(url, params)


def ecc_sign(rawhash, key):
    pk = coincurve.PrivateKey(key)
    signature = pk.sign_recoverable(rawhash, hasher=None)
    signature = base64.b64encode(signature)
    return signature


def hmacsha256(message):
    bmsg = str.encode(message)
    return hmac.new(key=b'', msg=bmsg, digestmod=hashlib.sha256).digest()


def sign(params, method, host_url, request_path, secret_key):
    encode_params = urllib.parse.urlencode(params)
    payload = [method, host_url, request_path, encode_params]
    payload = '\n'.join(payload)
    hashed = hmacsha256(payload)
    return ecc_sign(hashed, binascii.unhexlify(secret_key))
