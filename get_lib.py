'''
Created on 2019年4月25日

@author: xli45
'''
import datetime
from jqdatasdk import *
from jqdatasdk import finance

def time_handle(intervel):
    begin_time=(datetime.datetime.now()-datetime.timedelta(days=intervel)).strftime('%Y-%m-%d')
    return begin_time


def jukuan_login():
    auth('18925229395', 'daminghu1981')
    
    
def get_today():
    return (datetime.datetime.now()).strftime('%Y-%m-%d')


def dfdate_xueqiu(code,day_number):
    return finance.run_query(query(finance.STK_XUEQIU_PUBLIC).filter(finance.STK_XUEQIU_PUBLIC.code==code).order_by(finance.STK_XUEQIU_PUBLIC.day.desc()).limit(day_number))


def dfdate_price(code,start_date,end_date):
     
    return get_price(code,start_date,end_date,frequency='daily',fields=['open','close']).sort_index(axis = 0,ascending = False)

def code_transfer(code):
    
    fff=code[0:6]
    return fff
   