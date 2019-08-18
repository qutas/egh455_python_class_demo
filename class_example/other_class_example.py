#!/usr/bin/env python

from .class_example import ClassExample

class OtherClassExample(ClassExample):
	def __init__(self):
		super().__init__()

		self.CONST_VAL = 10

