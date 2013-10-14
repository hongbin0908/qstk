'''
@author: Bin Hong
@summary: homework1. http://wiki.quantsoftware.org/index.php?title=CompInvestI_Homework_1
'''

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

def perf(start, end, symbols, allocations):
    timeofday = dt.timedelta(hours=16)    
    timestamps = du.getNYSEdays(start, end, timeofday)
    c_dataobj = da.DataAccess('Yahoo')
    keys = ['close']
    data = c_dataobj.get_data(timestamps, symbols, keys)
    data = data[0].values

    rets = data / data[0, :]
    tsu.returnize0(rets)
    print rets
    
def main():
    ls_symbols=['GOOG', 'AAPL', 'GLD', 'XOM']
    ls_allocations = ['0.2', '0.2', '0.3', '0.3']
    #update_symbols(ls_symbols)
    dt_start = dt.datetime(2010,1,1)
    dt_end = dt.datetime(2013,9,30)

    perf(dt_start, dt_end, ls_symbols, ls_allocations)

    
    
if __name__ == '__main__':
    main()
