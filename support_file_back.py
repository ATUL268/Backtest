# import zrd_login
# kite = zrd_login.kite
from pprint import pprint
import pdb
import pandas as pd
import support_file_back as get
import datetime
import time
from datetime import datetime
from nsepython import *






def LTP(name):

	zrd_name = 'NSE:'+ name
	data = kite.quote([zrd_name])
	ltp = data[zrd_name]['last_price']
	return ltp

def OPENN(name):
	openn = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['open']
	return openn

def HIGH(name):
	high = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['high']
	return high

def LOW(name):
	low = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['low']
	return low

def CLOSE(name):
	close = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['close']
	return close

def BID(name):
	bid_price = kite.quote(['NSE:'+ name])['NSE:'+ name]['depth']['buy'][0]['price']
	return bid_price

def ASK(name):
	Ask_price = kite.quote(['NSE:'+ name])['NSE:'+ name]['depth']['sell'][0]['price']
	return Ask_price


def VOLUME(name):
	volume = kite.quote(['NSE:'+ name])['NSE:'+ name]['volume']
	return volume


def l_ohlc_v(name):
	zrd_name = 'NSE:'+ name
	data = kite.quote([zrd_name])
	ltp = data[zrd_name]['last_price']
	openn = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['open']
	high = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['high']
	low = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['low']
	close = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['close']
	volume = kite.quote(['NSE:'+ name])['NSE:'+ name]['volume']
	return ltp,openn,high,low,close,volume


def ob():
	margins = kite.margins()
	ob = margins['equity']['available']['opening_balance']
	return ob

def ohlc(name):
	
	openn = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['open']
	high = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['high']
	low = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['low']
	close = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['close']
	
	return openn,high,low,close,


def BID_1(name):
	data = kite.quote('NSE:' + name)
	bid_price = data['NSE:'+name]['depth']['buy'][0]['price']
	return bid_price


def lb():
	margins = kite.margins()
	lb = margins['equity']['available']['live_balance']
	return lb

def pnl(name):
	sym = name
	pos = kite.positions()
	net_pos = pos['net']
	len_net_pos = len(net_pos)

	for x in range(len_net_pos):
		if net_pos[x]['tradingsymbol']==sym:
			pnl = (round(pos['net'][x]['pnl'],2))
			return pnl

	
def net_pnl():
	traded_stocks_pnl = []
	pos = kite.positions()
	net_pos = pos['net']
	len_net_pos = len(net_pos)

	for x in range(len_net_pos):
		a = round(net_pos[x]['pnl'],2)
		traded_stocks_pnl.append(a)
	value = (sum(traded_stocks_pnl))
	return value


def day_pnl():
	traded_stocks_pnl = []
	pos = kite.positions()
	net_pos = pos['day']
	len_net_pos = len(net_pos)

	for x in range(len_net_pos):
		a = round(net_pos[x]['pnl'],2)
		traded_stocks_pnl.append(a)
	value = (sum(traded_stocks_pnl))
	return value

def LTP_NFO(name):

	zrd_name = 'NFO:'+ name
	data = kite.quote([zrd_name])
	ltp = data[zrd_name]['last_price']
	return ltp

def BID_NFO(name):
	bid_price = kite.quote(['NFO:'+ name])['NFO:'+ name]['depth']['buy'][0]['price']
	return bid_price


def expiry():
	Expiry = datetime.datetime.now().strftime("%y") + datetime.datetime.now().strftime("%b").upper()
	return Expiry

step_value = {'AARTIIND':20,'ACC':20,'ADANIENT':10,'ADANIPORTS':10,'AMARAJABAT':10,'AMBUJACEM':5,'APOLLOHOSP':50,'APOLLOTYRE':2.5,'ASHOKLEY':2.5,'ASIANPAINT':20,'AUROPHARMA':10,'AXISBANK':10,'BAJAJ-AUTO':50,'BAJAJFINSV':100,'BAJFINANCE':100,'BALKRISIND':20,'BANDHANBNK':10,'BANKBARODA':1,'BATAINDIA':20,'BEL':2.5,'BERGEPAINT':10,'BHARATFORG':10,'BHARTIARTL':10,'BHEL':1,'BIOCON':5,'BOSCHLTD':250,'BPCL':5,'BRITANNIA':50,'CADILAHC':5,'CANBK':2.5,'CHOLAFIN':10,'CIPLA':10,'COALINDIA':2.5,'COFORGE':50,'COLPAL':20,'CONCOR':5,'CUMMINSIND':10,'DABUR':5,'DIVISLAB':50,'DLF':5,'DRREDDY':50,'EICHERMOT':50,'ESCORTS':20,'EXIDEIND':2.5,'FEDERALBNK':1,'GAIL':2.5,'GLENMARK':10,'GMRINFRA':1,'GODREJCP':10,'GODREJPROP':20,'GRASIM':10,'HAVELLS':10,'HCLTECH':10,'HDFC':20,'HDFCAMC':20,'HDFCBANK':20,'HDFCLIFE':10,'HEROMOTOCO':50,'HINDALCO':5,'HINDPETRO':5,'HINDUNILVR':20,'IBULHSGFIN':5,'ICICIBANK':10,'ICICIGI':20,'ICICIPRULI':10,'IDEA':1,'IDFCFIRSTB':1,'IGL':5,'INDIGO':20,'INDUSINDBK':20,'INFRATEL':5,'INFY':20,'IOC':1,'ITC':2.5,'JINDALSTEL':5,'JSWSTEEL':5,'JUBLFOOD':50,'KOTAKBANK':20,'L&TFH':2.5,'LALPATHLAB':50,'LICHSGFIN':10,'LT':20,'LUPIN':10,'M&M':10,'M&MFIN':5,'MANAPPURAM':2.5,'MARICO':5,'MARUTI':100,'MCDOWELL-N':10,'MFSL':10,'MGL':20,'MINDTREE':20,'MOTHERSUMI':2.5,'MRF':500,'MUTHOOTFIN':20,'NATIONALUM':1,'NAUKRI':100,'NESTLEIND':100,'NMDC':2.5,'NTPC':1,'ONGC':1,'PAGEIND':500,'PEL':20,'PETRONET':5,'PFC':2.5,'PIDILITIND':20,'PNB':1,'POWERGRID':2.5,'PVR':20,'RAMCOCEM':10,'RBLBANK':5,'RECLTD':2.5,'RELIANCE':20,'SAIL':1,'SBILIFE':10,'SBIN':5,'SHREECEM':250,'SIEMENS':20,'SRF':50,'SRTRANSFIN':20,'SUNPHARMA':10,'SUNTV':10,'TATACHEM':10,'TATACONSUM':10,'TATAMOTORS':5,'TATAPOWER':1,'TATASTEEL':10,'TCS':20,'TECHM':10,'TITAN':20,'TORNTPHARM':50,'TORNTPOWER':5,'TVSMOTOR':10,'UBL':20,'ULTRACEMCO':50,'UPL':10,'VEDL':2.5,'VOLTAS':10,'WIPRO':5,'ZEEL':5,}
index_step_value ={'NIFTY 50': 75, 'NIFTY BANK': 25}

def option_name_atm(name,ce_pe):
	ltp = LTP(name)
	sv = step_value[name]
	atm_strike = round(ltp/sv)*sv
	option_name = name + expiry()+ str(atm_strike)+ce_pe
	return option_name


def option_name(name,ce_pe,multiplier):
	ltp = LTP(name)
	sv = step_value[name]
	atm_strike = round(ltp/sv)*sv+sv*multiplier
	option_name = name + expiry()+ str(atm_strike)+ce_pe
	return option_name


def get_fno_data(name, delta, interval,oi):

	token =  kite.ohlc([name])[name]['instrument_token']
	to_date = datetime.datetime.now().date()
	from_date = to_date - datetime.timedelta(days=delta)
	data = kite.historical_data(instrument_token=token, from_date=from_date, to_date=to_date, interval=interval,  oi=True)
	df = pd.DataFrame(data)	
	return df

def get_equity_data(name, segment, delta, interval, continuous, oi):

	token = kite.ltp([segment + name])[segment + name]['instrument_token']
	to_date = datetime.datetime.now().date()
	from_date = to_date - datetime.timedelta(days=delta)

	data = kite.historical_data(instrument_token=token, from_date=from_date, to_date=to_date, interval=interval, continuous=False, oi=False)
	df = pd.DataFrame(data)
	# df = df.set_index(df['date'])
	return df

def read_data(name):

	this_add = '21JUNFUT'
	next_add = '21JULFUT'

	this_name = name + this_add + '.csv'
	next_name =  name + next_add + '.csv'

	this = pd.read_csv('this' + '\\'+ this_name)
	nextt = pd.read_csv('next' + '\\'+ next_name)

	this =  this.set_index(this['date'])
	nextt = nextt.set_index(nextt['date'])

	return this,nextt

# 2022

def get_good_values(name):

	zrd_name = 'NSE:' + name
	data = kite.quote([zrd_name])

	ltp = data[zrd_name]['last_price']
	openx = data[zrd_name]['ohlc']['open']
	high = data[zrd_name]['ohlc']['high']
	low = data[zrd_name]['ohlc']['low']
	close = data[zrd_name]['ohlc']['close']
	# volume = data[zrd_name]['volume']

	return ltp, openx, high, low, close

def wd():

	trade_day = {'Monday' : {'stop_loss': 0.06, 'target': 0.84},'Tuesday' : {'stop_loss': 0.60, 'target': 0.70},'Wednessday' : {'stop_loss': 0.20, 'target': 0.95},'Thrusday' : {'stop_loss': 0.14, 'target': 0.84},'Friday' : {'stop_loss': 0.06, 'target': 0.84},}
	week_day = datetime.today().strftime('%A')
	sl = trade_day[week_day]['stop_loss']
	tgt = trade_day[week_day]['target']
	print(week_day)
	return sl ,tgt


def convert(date_time):
    format = "%d-%b-%Y"# The format
    datetime_str = datetime.datetime.strptime(date_time, format)
 
    return datetime_str


def current_expiry():
	

	expiry_status = {}
	year = datetime.datetime.now().year
	month =datetime.datetime.now().month
	day = datetime.datetime.now().day

	test_date = datetime.datetime(year, month, day)
	nxt_mnth = test_date.replace(day=28) + datetime.timedelta(days=4)
	res = nxt_mnth - datetime.timedelta(days=nxt_mnth.day)
	last_day_month = (res.day)

	index_list_from_nse = (indices)

	data_from_nse = expiry_list(index_list_from_nse[2])

	for name in data_from_nse:

		date_time = name
		soso = get.convert(date_time)
		soso = str(soso)
		month_cut_soso =soso[6:7]
		year_cut_soso = soso[2:4]

		new_name = name[0:2]
		expiry_date = int(new_name)

		if (last_day_month - expiry_date) > 7:
			# print('weekly_expiry')

			# year = str(year)
			# year = year[2:4]
			# month = str(month)
			expiry_weekly = ( year_cut_soso + month_cut_soso + name[0:2])
			expiry_status[name] = expiry_weekly
			year = datetime.datetime.now().year
			# print(expiry_status)



		if (last_day_month - expiry_date) < 7:
			# print('Monthly_expiry')

			# year = str(year)
			# year = year[2:4]
			month_first_3 = str(datetime.datetime.now().strftime("%b").upper())
			
			expiry_monthly = ( year_cut_soso + month_first_3)
			expiry_status[name] = expiry_monthly

			year = datetime.datetime.now().year


	current_expiry = data_from_nse[0]


	return expiry_status[current_expiry]


def next_expiry():
	

	expiry_status = {}
	year = datetime.datetime.now().year
	month =datetime.datetime.now().month
	day = datetime.datetime.now().day

	test_date = datetime.datetime(year, month, day)
	nxt_mnth = test_date.replace(day=28) + datetime.timedelta(days=4)
	res = nxt_mnth - datetime.timedelta(days=nxt_mnth.day)
	last_day_month = (res.day)

	index_list_from_nse = (indices)

	data_from_nse = expiry_list(index_list_from_nse[2])

	for name in data_from_nse:

		date_time = name
		soso = get.convert(date_time)
		soso = str(soso)
		month_cut_soso =soso[6:7]
		year_cut_soso = soso[2:4]

		new_name = name[0:2]
		expiry_date = int(new_name)

		if (last_day_month - expiry_date) > 7:
			# print('weekly_expiry')

			# year = str(year)
			# year = year[2:4]
			# month = str(month)
			expiry_weekly = ( year_cut_soso + month_cut_soso + name[0:2])
			expiry_status[name] = expiry_weekly
			year = datetime.datetime.now().year
			# print(expiry_status)



		if (last_day_month - expiry_date) < 7:
			# print('Monthly_expiry')

			# year = str(year)
			# year = year[2:4]
			month_first_3 = str(datetime.datetime.now().strftime("%b").upper())
			
			expiry_monthly = ( year_cut_soso + month_first_3)
			expiry_status[name] = expiry_monthly

			year = datetime.datetime.now().year


	current_expiry = data_from_nse[1]


	return expiry_status[current_expiry]



def get_data_range(name,segment,delta,delta1,interval,continuous,oi):
	token = kite.ltp([segment + name])[segment + name]['instrument_token']
	to_date = datetime.datetime.now().date()
	to_date1 = to_date - datetime.timedelta(days = delta1)
	from_date = to_date - datetime.timedelta(days = delta)
	hd = kite.historical_data(instrument_token = token, from_date = from_date, to_date = to_date1, interval = interval, continuous = False, oi = False)
	hd = pd.DataFrame(hd)
	return hd