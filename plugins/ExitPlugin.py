#!/usr/bin/env python

from Module import *

####################################################################
# 
# 
####################################################################
class Plugin(Module):
	def __init__(self):
		Module.__init__(self,'safe_word')
		self.intent = 'safe_word'
			
	def process(self, entity):
		return 'exit_loop'


if __name__ == '__main__':
	e = ExitModule
	
	print 'bye ...'
	