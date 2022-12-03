import zrd_login
kite = zrd_login.kite
from pprint import pprint
import pdb
import pandas as pd
import support_file_back as get
import datetime
import time
from datetime import datetime
import os ,time
from dateutil.parser import parse
import xlwings as xw
import talib
import random

status = {'traded_buy' : None,'traded_sell' : None, 'buy_ltp': None,'sell_ltp': None, 'index_Buy':None , 'index_Sell':None , 'pnl' : None , 'Drawdown' : None}
final_result = {}
trade_no = 0
cumulative = []

ma_small_value  = 20
ma_big_value  = 50
qty = 50


input_file  = (r"F:\code_atul\Code_back\file")
os.chdir(input_file)

files_list  = os.listdir(input_file)
original_file = files_list[0]

df = pd.read_csv(original_file)
df = df.set_index(df['date'])



df['ma_small'] = talib.EMA(df['close'], timeperiod=ma_small_value)
df['ma_big'] = talib.EMA(df['close'], timeperiod=ma_big_value)
df['ma_small_pre'] = df['ma_small'].shift(1)
df['ma_big_pre'] = df['ma_big'].shift(1)


for index, ohlc in df.iterrows():
	# print(index)

	ma_s  =  round(df.loc[index]['ma_small'] , 2)
	ma_b = round(df.loc[index]['ma_big'] , 2)
	pre_ma_s = round(df.loc[index]['ma_small_pre'] , 2)
	pre_ma_b = round(df.loc[index]['ma_big_pre'] , 2)

	openn  =  df.loc[index]['open']
	# pdb.set_trace()


	if (ma_s > ma_b) and (status['traded_buy'] == None) and (pre_ma_s < ma_b) :


		status['traded_buy'] =  'Yes'
		status['buy_ltp'] = openn
		status['index_Buy'] = index[0:16]
		
		# pdb.set_trace()


	if (ma_s < ma_b) and (status['traded_sell'] == None) and (pre_ma_s > ma_b) :


		status['traded_sell'] =  'Yes'
		status['sell_ltp'] = openn
		status['index_Sell'] = index[0:16]



	if (status['traded_sell'] == 'Yes') and (status['traded_buy'] == 'Yes') :

		pnl = round(status['sell_ltp'] - status['buy_ltp'] , 2 ) * qty

		status['pnl'] = pnl
		trade_no = trade_no + 1
		print(trade_no)
		cumulative.append(status['pnl'])

		status['Drawdown'] = sum(cumulative)

		final_result[trade_no] = status
		status = {'traded_buy' : None,'traded_sell' : None, 'buy_ltp': None,'sell_ltp': None, 'index_Buy':None , 'index_Sell':None , 'pnl' : None , 'Drawdown' : None}

		res = pd.DataFrame(final_result).T
		print(res)
		pdb.set_trace()
# print(max(cumulative))
# print(min(cumulative))

# num = random.random()

# num = str(num)



# os.chdir(r"F:\code_atul\Code_back\result_storage")
# res.to_excel(num + 'Result.xlsx')





		







# 		   trade_no = trade_no + 1
# 		final_result[trade_no] = status

# 		status = {'traded_buy' : None,'traded_sell' : None ,'sell_ltp' : None,'index':None}















res = pd.DataFrame(final_result).T

res.to_excel('result11.xlsx')




	# if ma_s < ma_b :
	# 	print(index)
	# 	print(close)










