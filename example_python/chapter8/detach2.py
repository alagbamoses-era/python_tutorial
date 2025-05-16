#!/usr/bin/python3


import io

text1 = io.TextIOWrapper(io.BytesIO(b'Hello Moses'), encoding="utf-8")

buf = text1.detach()

print(buf.read())




