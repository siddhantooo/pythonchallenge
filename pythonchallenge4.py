# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: Siddhant
"""
#import pandas as pd
#import matplotlib.pyplot as plt
#import statsmodels as sm
#import numpy as np
import urllib as url

f = open('pythonchallenge4links.txt','w')
nothing = 8743
path = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
for i in range(400):
	req = url.request.Request(path+str(nothing), headers={'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
	nothing = url.request.urlopen(req).read()[-5:].strip().decode("utf-8")
	print(url.request.urlopen(req).read())
	f.write(url.request.urlopen(req).read().decode("utf-8")  + '\n')
	print(nothing,"i",i)
f.close()
if __name__ == '__main__':
    from time import clock as clock
    start_time = clock()

    end_time = clock()
    print("It took the program", int((end_time-start_time)//3600), "hour(s)", int(((end_time-start_time)//60)%60), "minute(s)",  '{:f}'.format(((end_time-start_time)%3600)%60),"seconds to run.")















