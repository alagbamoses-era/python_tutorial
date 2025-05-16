#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


key = get_random_bytes(16)
msg = b'Hello World'

cipher = AES.new(key, AES.MODE_CBC)
encrypted = cipher.encrypt(pad(msg, AES.block_size))

ciphertext = base64.b64encode(iv + encrypted)

print('Encrypted: ', ciphertext.decode())
