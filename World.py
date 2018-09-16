

import time

import math


class World():

	def _init_(self):
		self.pitch = 0
		self.roll = 0
		
	def readFile(self, f1):
			 file = open(f1,"r")
			 for line in file:
							print line

