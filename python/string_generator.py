#!/usr/bin/python

import string	
import os
import collections

for i in xrange(1,26):
	for j in xrange(1,26):
		for k in xrange(1,26):
			for l in xrange(1,26):
				a=string.ascii_lowercase[i]
				b=string.ascii_lowercase[j]
				c=string.ascii_lowercase[k]
				d=string.ascii_lowercase[l]
				str_wait=a+b+c+d
				# print str_wait
				# type(str_wait)
				max_count=collections.Counter(str_wait).most_common(1)[0][1]
				if max_count == 3:
					print str_wait






				# if j > 1:
				# 	os._exit(0)
					
