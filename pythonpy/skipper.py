__author__ = 'jianjiang'
#! /usr/bin/python3
# -*- coding: utf8 -*-

class SkipIterator:
	def __init__(self,wrapped):
		self.wrapped=wrapped
		self.offset=0		# 偏移量为0
	@property
	def __next__(self):
		if self.offset>=len(self.wrapped):
			raise StopIteration		# 偏移量大于传入字符串的长度时，抛出异常
		else:
			item=self.wrapped[self.offset]		# 在传入字符串长度范围内，将wrapped[offset]赋给item
			self.offset+=2			# 偏移量向后推进2
			return item				# 返回item值

class SkipObject:
	def __init__(self,wrapped):
		self.wrapped=wrapped
	def __iter__(self):
		return SkipIterator(self.wrapped)

if __name__=='__main__':
	alpha='abcdef'
	skipper=SkipObject(alpha)
	I=iter(skipper)
	print(next(I),next(I),next(I))		# 偏移量依次为0 2 4

	for x in skipper:				# 自动调用函数__iter__
		for y in skipper:
			print(x+y,end=' ')