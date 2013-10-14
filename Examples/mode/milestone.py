#!/usr/bin/env python

'''
find the when:
1. the open is lowest and high is the close
2. bull more than 2%

to see then trend of the next 2 day
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def gain(item):
    p_open = item['open']
    p_close = item['close']
    return (p_close - p_open)/p_open
def isHandleShap(item, isSun=False):
    p_open = item['open']
    p_close = item['close']
    p_high = item['high']
    p_low = item['low']
    
    if p_open * p_close * p_high * p_low == 0:
        return False
    
    if isSun and p_open > p_close:
        return False
    p_top = p_high - max(p_open,p_close)
    p_mid = abs(p_close - p_open)
    p_bot = min(p_close, p_open) - p_low

    if p_bot == 0:
        return False
    if (p_top > p_mid):
        return False
    if (p_mid * 3 > p_bot):
        return False

    return True
def isSunShap(item):
    p_open = item['open']
    p_close = item['close']
    p_high = item['high']
    p_low = item['low']
    
    if p_open * p_close * p_high * p_low == 0:
        return False
    if p_open > p_close:
        return False
    p_top = p_high - max(p_open,p_close)
    p_mid = abs(p_close - p_open)
    p_bot = min(p_close, p_open) - p_low

    if p_mid == 0:
        return False
    if (p_top * 4 > p_mid):
        return False
    if (p_bot * 4 > p_mid):
        return False

    return True
def isCloudShap(item):
    p_open = item['open']
    p_close = item['close']
    p_high = item['high']
    p_low = item['low']
    
    if p_open * p_close * p_high * p_low == 0:
        return False
    if p_open < p_close:
        return False
    p_top = p_high - max(p_open,p_close)
    p_mid = abs(p_close - p_open)
    p_bot = min(p_close, p_open) - p_low

    if p_mid == 0:
        return False
    if (p_top * 4 > p_mid):
        return False
    if (p_bot * 4 > p_mid):
        return False

    return True


def get_his_data(symbol, dt_start, dt_end):
    dt_timeclose = dt.timedelta(hours=16)
    ldt_timecloses = du.getNYSEdays(dt_start, dt_end, dt_timeclose)
    
    c_dataobj = da.DataAccess('Yahoo')
    
    ls_keys = ['open','high', 'low', 'close','volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timecloses, [symbol], ls_keys)

    his_index = ldf_data[0].index
    
    his_values = np.zeros((len(his_index),len(ls_keys)))

    for i in range(len(ls_keys)):
        his_values[:,i] = ldf_data[i].values[:,0]
        his_data = pd.DataFrame(his_values, index=his_index, columns=ls_keys)
    his_data = his_data.fillna(0)
    return his_data

def main():
    """ main function"""
    dt_start = dt.datetime.now().date() - dt.timedelta(days=365)
    dt_end   = dt.datetime.now().date() - dt.timedelta(days=1)

    c_dataobj = da.DataAccess('Yahoo', verbose = True)
    ls_symbols = c_dataobj.get_all_symbols()
    
    sumd=0
    time = 0
    time_bull = 0;
    time_bear = 0;
    for symbol in ls_symbols:
        his_data = get_his_data(symbol, dt_start, dt_end)
        i = 0;
        for items in his_data.iterrows():
            close15 = his_data.ix[his_data.index[i-15]]['close']
            close5 = his_data.ix[his_data.index[i-5]]['close']
            item1 = his_data.ix[his_data.index[i-1]]
            close1 = his_data.ix[his_data.index[i-1]]['close']
            close0 = items[1]['close']
            if isHandleShap(items[1], True) and close1 >= close0 :
                if i+2 < len(his_data.index):
                    gains =  gain(his_data.ix[his_data.index[i+1]])
                    gains += gain(his_data.ix[his_data.index[i+2]])
                    if abs(gains) >0.1:
                        print symbol, items[0]
                    else:
                        if gains >= 0:
                            time_bull += 1
                        else:
                            time_bear += 1
                        sumd += gains
                        time += 1
                else: 
                    print symbol, items[0] 
            i += 1
    print sumd/time, time, float(time_bull)/time
if __name__ == '__main__':
    main()
