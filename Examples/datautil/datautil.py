#!/usr/bin/env python
import sys,os

local_path = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(local_path + "/./")

''' Python imports '''
import datetime as dt

''' 3rd party imports '''
import numpy as np
import pandas as pand

''' QSTK imports '''
from QSTK.qstkutil import DataAccess as da
from QSTK.qstkutil import qsdateutil as du

def get_data0():
    lsSym = ['AA', 'AXP', 'BA' ]
    lsSym.append('$SPX')
    ''' Get data for 2009-2013 '''
    dtStart = dt.datetime(2010,9,20)
    dtEnd = dt.datetime(2010,9,30)
    
    norObj = da.DataAccess('Yahoo')      
    ldtTimestamps = du.getNYSEdays( dtStart, dtEnd, dt.timedelta(hours=16) )
    
    lsKeys = ['open', 'high', 'low', 'close', 'volume']
    ldfData = norObj.get_data( ldtTimestamps, lsSym, lsKeys )
    dData = dict(zip(lsKeys, ldfData))
    return dData
if __name__ == '__main__':
    main()
