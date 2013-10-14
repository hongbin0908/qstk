#!/usr/bin/env python
#!/usr/bin/env python
import sys,os
 
local_path = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(local_path + "/../datautil/")

import datautil

''' Python imports '''
import datetime as dt

''' 3rd party imports '''
import numpy as np
import pandas as pand
import matplotlib.pyplot as plt

''' QSTK imports '''
from QSTK.qstkutil import DataAccess as da
from QSTK.qstkutil import qsdateutil as du

from QSTK.qstkfeat.features import featMA, featRSI,featAroon, featBeta, featCorrelation, featBollinger,featStochastic
from QSTK.qstkfeat.classes import class_fut_ret
import QSTK.qstkfeat.featutil as ftu

def main():
    ''' Use Dow 30 '''
    lsSym = ['AA', 'AXP', 'BA', 'BAC', 'CAT', 'CSCO', 'CVX', 'DD', 'DIS', 'GE', 'HD', 'HPQ', 'IBM', 'INTC', 'JNJ','JPM', 'KFT', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'PFE', 'PG', 'T', 'TRV', 'UTX', 'WMT', 'XOM' ]
    lsSym.append('$SPX')
    ''' Get data for 2009-2010 '''
    dtStart = dt.datetime(2010,8,01)
    dtEnd = dt.datetime(2010,12,31)
    
    norObj = da.DataAccess('Yahoo')      
    ldtTimestamps = du.getNYSEdays( dtStart, dtEnd, dt.timedelta(hours=16) )
    
    lsKeys = ['open', 'high', 'low', 'close', 'volume']
    ldfData = norObj.get_data( ldtTimestamps, lsSym, lsKeys )
    dData = dict(zip(lsKeys, ldfData))
    print  dData['close']['AA']
    dRel = ftu.getMarketRel(dData, sRel='$SPX')
    
def test_speedTest():
    ftu.speedTest([featMA, featRSI, featAroon, featBeta, featCorrelation, 
               featBollinger, featStochastic], [{'lLookback':30}] * 7)
def test_applyFeatures():
    dData = datautil.get_data0()
    ldfFeatures = ftu.applyFeatures(dData, [featMA], [{'lLookback':2}])
    print ldfFeatures
    ldfFeatures = ftu.stackSyms(ldfFeatures)
    print ldfFeatures
    ftu.normFeatures(ldfFeatures,-1,1,False)
    
if __name__ == '__main__':
    test_applyFeatures()
    
