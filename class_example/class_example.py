#!/usr/bin/env python

class ClassExample():
	CONST_VAL = 2

	def __init__(self):
		self.CONST_OTHER_VAL = 4

	def get_const_val(self):
		return self.CONST_VAL

	def get_const_val(self):
		return self.CONST_OTHER_VAL

	def process_val(self, val):
		return self.CONST_VAL * val

	def process_other_val(self, val):
		return self.CONST_OTHER_VAL * val

