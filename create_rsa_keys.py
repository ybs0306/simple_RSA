#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'kinoshitakenta'
__email__ = 'ybs0306748@gmail.com'
# reference by https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/368805/

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

# 偽隨機數生成器
random_generator = Random.new().read
# rsa演算法生成例項
rsa = RSA.generate(1024, random_generator)

# master的祕鑰對的生成
private_pem = rsa.exportKey()
with open('master-private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'wb') as f:
    f.write(public_pem)

'''
# ghost的祕鑰對的生成
private_pem = rsa.exportKey()
with open('master-private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'wb') as f:
    f.write(public_pem)
'''
