#!/usr/bin/python
# -*- coding: utf-8 -*-

class Token(object):
	def __init__(self, tokenType, content):
		self.type = tokenType
		self.content = content

	def __init__(self, tokenType):
		self.type = tokenType
		self.content = ""

	@staticmethod
	def equalType(token1, token2):
		if token1.type == token2.type:
			return True
		return False

	@staticmethod
	def equal(token1, token2):
		if equalType(token1, token2):
			if token1.content == token2.content:
				return True
		return False

if __name__ == '__main__':
    pass
