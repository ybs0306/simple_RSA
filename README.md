### 這個repo是啥

- 這是一個簡單的RSA公私鑰生成與加密解密測試
- 把txt檔加密之後再解密
<br>

## usage
所以檔案都放同一個目錄底下

> 因為會用到Crypto所以記得裝
```
$ pip install pycrypto
```
<br>

- 生成RSA keys，會生成 **master-public.pem** 與 **master-private.pem** 兩個檔案
```
$ python3 create_rsa_keys.py
```

- 對檔案進行加密
```
$ python3 file_encryption.py 原檔檔名 加密檔檔名
```

- 對檔案進行解密
```
$ python3 file_decryption.py 加密檔檔名 解密檔檔名
```
