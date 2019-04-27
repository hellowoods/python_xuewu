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

##################################################################################

df_XQ_data=dfdate_xueqiu(code,day_number)#雪球数据
 
df_XQ_data.to_csv('xueqiu.csv',index=True)

df_JG_data= dfdate_price(code,day_number,date_today)#价格数据

df_JG_data.to_csv('hangqing.csv',index=True)

##################################################################################
#把df_hangqing中的两列加入df_xueqiu  思路：先把数据按列分割提取，然后再把分出去的列重新插入
date_open =pd.read_csv('hangqing.csv').pop('open')
date_close =pd.read_csv('hangqing.csv').pop('close')
##################################################################################
column_id=df_XQ_data.columns.tolist()
df_XQ_data.insert(column_id.index('new_trade')+1,'open',date_open)
df_XQ_data.insert(column_id.index('new_trade')+2,'close',date_close)
##################################################################################
code_name=code_transfer(code)+'.csv'
df_XQ_data.to_csv("./300/%s"%code_name)

print('ok')

# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
df_JG_data['close'].plot() 
plt.show()



