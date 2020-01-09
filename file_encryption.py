#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'kinoshitakenta'
__email__ = 'ybs0306748@gmail.com'
# reference by https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/368805/

import sys
import os
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA

def exit_process(msg):
    print(msg)
    sys.exit()

# 檢查參數跟檔案有沒有問題
if len(sys.argv) != 3:
    exit_process('給的參數數量不對喔')
if not os.path.isfile(sys.argv[1]):
    exit_process('要加密的檔案不存在呦')
if not os.path.isfile('master-public.pem'):
    exit_process('public key檔案不存在呦')

try:
    # 讀原檔
    with open(sys.argv[1], 'r', encoding='utf8') as f:
        msg = ''
        for line in f:
            msg = msg + line

    # 讀金鑰檔案
    with open('master-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        # 字串轉成byte格式
        msg_b = bytes(msg, encoding = 'utf8')
        cipher_text = base64.b64encode(cipher.encrypt(msg_b))
        print(cipher_text)

    # 寫成加密檔
    with open(sys.argv[2], 'w') as f:
        # byte轉回utf8格式寫進檔案
        f.write(cipher_text.decode())

except Exception as e:
    print(f'不知道為啥 可是有bug爆開了\n{e}')
