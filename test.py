#coding=utf-8
import datetime
import datetime
from jqdatasdk import *
from jqdatasdk import finance
from get_lib import *
code='600175.XSHG'
date_today=get_today()
# import numpy as np 
# from matplotlib import pyplot as plt 
#  
# x = np.arange(1,11) 
# y =  2  * x +  5 
# print(x)
# # plt.title("Matplotlib demo") 
# # plt.xlabel("x axis caption") 
# # plt.ylabel("y axis caption") 
# plt.plot(x,y) 
# plt.show()

dae=(datetime.datetime.now()).strftime('%Y-%m-%d')
auth('18925229395', 'daminghu1981')
ddd=get_price('600175.XSHG', 20, end_date='2019-04-26', frequency='daily', fields=['open', 'close']).sort_index(axis = 0,ascending = False)
#ddd=dfdate_price(code,20,'2019-4-26')
print(ddd)
