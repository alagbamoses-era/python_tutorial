#!/usr/bin/python3


import sys

raw_out = sys.stdout.detach()

raw_out.write(b'Hello Moses\n')
