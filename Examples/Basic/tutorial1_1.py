#!/usr/bin/env python

#############################
# author hongbin0908@126.com
# a tutorial of QSTK 1. plot the close price of stock SPY, DVN, TLT
#############################

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import QSTK.qstktools.YahooDataPull as dp
# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


def update_symbols(symbols):
    '''
    Update the data of sysmbol in the root dir
    '''
    c_dataobj = da.DataAccess('Yahoo', verbose=True)
    s_path = c_dataobj.rootdir
    
    ls_missed_sysms = dp.get_yahoo_data(s_path, symbols)

    if (len(ls_missed_sysms) > 0):
        dp.get_yahoo_data(s_path, ls_missed_sysms)
def main():
    ls_symbols = ['TLT', 'SPY', 'DVN', 'JPM']
    #update_symbols(ls_symbols)
    
    #dt_start = dt.date.today()  - dt.timedelta(days=7)
    #dt_end = dt.date.today() - dt.timedelta(days=1)

    dt_start = dt.datetime(2010, 1, 1)
    dt_end = dt.datetime(2013, 9, 30)
    dt_timeofday = dt.timedelta(hours=16)

    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    c_dataobj = da.DataAccess('Yahoo')

    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    
    d_data = dict(zip(ls_keys, ldf_data))
    
    plt.clf()
    plt.plot(ldt_timestamps, d_data['close'].values)
    plt.legend(ls_symbols)
    plt.ylabel('close')
    plt.xlabel('date')
    plt.savefig('tutorial1_1.close.pdf', format='pdf')

    plt.clf()
    na_price = d_data['close'].values
    plt.plot(ldt_timestamps, na_price / na_price[0,:])
    plt.legend(ls_symbols)
    plt.ylabel('normalized close')
    plt.xlabel('date')
    plt.savefig('tutorial1_1.normalized_close.pdf', format='pdf')
    

if __name__ == '__main__':
    main()
