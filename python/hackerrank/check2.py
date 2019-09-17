#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if (n%2)==1: # n is odd
	print("Weird")
else:
	if n in range(2,6): #Inclusive
		print("Not Weird")
	elif n in range(6,21): #Inclusive
		print("Weird")
	elif n in range(20,101):
		print("Not Weird")
	else:
		pass