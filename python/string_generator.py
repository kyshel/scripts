#!/usr/bin/python
# Remote_version: https://github.com/kyshel/scripts/blob/master/python/string_generator.py
# Aim: 4 letters string, find ones that have three same character, eg 'aaab' is ok, 'aabc' is not
# Date: 170410
# Contact: kyshel.me

import string	
import os
import collections


text_file = open("out.txt", "w")

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
					text_file.write(str_wait+'\n')





text_file.close()
