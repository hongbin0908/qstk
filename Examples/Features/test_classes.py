#!/usr/bin/env python

''' Python imports '''
import datetime as dt

''' 3rd party imports '''
import numpy as np
import pandas as pand
import matplotlib.pyplot as plt

''' QSTK imports '''
from QSTK.qstkutil import DataAccess as da
from QSTK.qstkutil import qsdateutil as du

from QSTK.qstkfeat.features import featMA, featRSI
from QSTK.qstkfeat.classes import class_fut_ret

import QSTK.qstkfeat.classes as cls


def main():
    ''' Use Dow 30 '''
    lsSymTrain = ['AA','AXP'] + ['$SPX']
    lsSymTest = ['AA','AXP'] + ['$SPX']
	
    lsSym = list(set(lsSymTrain).union(set(lsSymTest)))
    
    dtStart = dt.datetime(2008,01,01)
    dtEnd = dt.datetime(2008,01,07)

    norObj = da.DataAccess('Yahoo')	  
    ldtTimestamps = du.getNYSEdays( dtStart, dtEnd, dt.timedelta(hours=16) )	
    
    lsKeys = ['open', 'high', 'low', 'close', 'volume']
    
    ldfData = norObj.get_data( ldtTimestamps, lsSym, lsKeys ) #this line is important even though the ret value is not used
	
    for temp in ldfData:
        temp.fillna(method="ffill").fillna(method="bfill")
    
    ldfDataTrain = norObj.get_data( ldtTimestamps, lsSymTrain, lsKeys )
    ldfDataTest = norObj.get_data( ldtTimestamps, lsSymTest, lsKeys)
    for temp in ldfDataTrain:
        temp.fillna(method="ffill").fillna(method="bfill")
		
    for temp in ldfDataTest:
        temp.fillna(method="ffill").fillna(method="bfill")
	
    dDataTrain = dict(zip(lsKeys, ldfDataTrain))
    dDataTest = dict(zip(lsKeys, ldfDataTest))

    cls.class_fut_ret(dDataTrain, 1)
    print dData['close']['AA']
if __name__ == '__main__':
    main()
