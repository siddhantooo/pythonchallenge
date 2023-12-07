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
import pickle
path = "http://www.pythonchallenge.com/pc/def/banner.p"
f = open('pythonchallenge5peakhell.txt','wb')
f.write(url.request.urlopen(path).read())
f.close()
#col = 'c0c0ff' #lavender blue

f = open('pythonchallenge5depickle.txt','w')
d = pickle.load(open('pythonchallenge5peakhell.txt','rb'))
print(d)
f.write(str(d))
f.close()



if __name__ == '__main__':
    from time import clock as clock
    start_time = clock()

    end_time = clock()
    print("It took the program", int((end_time-start_time)//3600), "hour(s)", int(((end_time-start_time)//60)%60), "minute(s)",  '{:f}'.format(((end_time-start_time)%3600)%60),"seconds to run.")















