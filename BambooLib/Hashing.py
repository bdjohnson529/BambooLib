#!/usr/bin/env python
# encoding: utf-8
"""
BambooLib - Hashing

Hashing functions

author : Ben Johnson
"""


# input any string
# output hashed string
def generate_uniqueid(input_str):
	m = hashlib.md5()
	m.update(input_str.encode('utf-8'))
	md5_hex = m.hexdigest()
	
	return md5_hex