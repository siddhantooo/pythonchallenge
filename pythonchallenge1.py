# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: Siddhant
"""
#import pandas as pd
#import matplotlib.pyplot as plt
#import statsmodels as sm
#import numpy as np
import string


def f():
    return None

def decode(text,l=list('abcdefghijklmnopqrstuvwxyz')):
	   decoded_text = ''
	   m = dict(zip(l,range(26)))
	   n = dict(zip(range(26),l))
	   for i in range(len(text)):
		   if text[i] in l:
			   decoded_text += n[(m[text[i]]+2)%26]
		   else:
			   decoded_text += text[i]
	   return(decoded_text)
print((decode("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")))