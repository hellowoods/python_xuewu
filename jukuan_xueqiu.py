#coding=utf-8
import pandas as pd
import numpy as np
from get_lib import *
import datetime
import numpy as np 
from matplotlib import pyplot as plt 

##################################################################################
jukuan_login()
################################################################################## 
code='600175.XSHG'
day_number=50
date_today=get_today()
#s_date=time_handle(day_number)
#print(date_today)
##################################################################################
# df=finance.run_query(query(finance.STK_XUEQIU_PUBLIC).filter(finance.STK_XUEQIU_PUBLIC.day==c_date).order_by(finance.STK_XUEQIU_PUBLIC.new_follower.desc()).limit(10))
df_xueqiu=dfdate_xueqiu(code,day_number)
 
df_xueqiu.to_csv('xueqiu.csv',index=True)

df_hangqing= dfdate_price(code,day_number,date_today)

df_hangqing.to_csv('hangqing.csv',index=True)

##################################################################################
#把df_hangqing中的两列加入df_xueqiu  思路：先把数据按列分割提取，然后再把分出去的列重新插入
date_open =pd.read_csv('hangqing.csv').pop('open')
date_close =pd.read_csv('hangqing.csv').pop('close')
##################################################################################
column_id=df_xueqiu.columns.tolist()
df_xueqiu.insert(column_id.index('new_trade')+1,'open',date_open)
df_xueqiu.insert(column_id.index('new_trade')+2,'close',date_close)
##################################################################################
code_name=code_transfer(code)+'.csv'
df_xueqiu.to_csv(code_name,index=False)

print('ok')

from matplotlib import pyplot as plt 
  

# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
df_hangqing.plot() 
plt.show()



