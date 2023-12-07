# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: Siddhant
"""
#import pandas as pd
#import matplotlib.pyplot as plt
#import statsmodels as sm
#import numpy as np
f = open('pythonchallenge6zip.txt','w')
nothing = '90052'
for i in range(911):
	if nothing != 'Collect the comments.':
		with open("C:\\Users/siddh/Downloads/Active/channel/"+nothing+'.txt', 'r') as g:
			text = g.read()
			nothing = text.split('nothing is ')[-1]
			print(text)
			f.write(text + '\n')
f.close()
if __name__ == '__main__':
    from time import clock as clock
    start_time = clock()

    end_time = clock()
    print("It took the program", int((end_time-start_time)//3600), "hour(s)", int(((end_time-start_time)//60)%60), "minute(s)",  '{:f}'.format(((end_time-start_time)%3600)%60),"seconds to run.")















