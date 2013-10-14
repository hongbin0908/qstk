''' Python imports '''
import datetime as dt

''' 3rd party imports '''
import numpy as np
import pandas as pand
import matplotlib.pyplot as plt

''' QSTK imports '''
from QSTK.qstkutil import DataAccess as da
from QSTK.qstkutil import qsdateutil as du


from QSTK.qstkfeat.classes import class_fut_ret
import QSTK.qstkfeat.featutil as ftu	
	
import sys
import time

from functions import *

if __name__ == '__main__':
	dDataTrain, dDataTest = get_data0()
	lfcFeatures,ldArgs = get_features0()
	
	''' Generate a list of DataFrames, one for each feature, with the same index/column structure as price data '''
	ldfFeaturesTrain = ftu.applyFeatures( dDataTrain, lfcFeatures, ldArgs, '$SPX')
	ldfFeaturesTest = ftu.applyFeatures( dDataTest, lfcFeatures, ldArgs, '$SPX')

	''' Pick Test and Training Points '''		
	dtStartTrain = dt.datetime(2008,01,01)
	dtEndTrain = dt.datetime(2009,12,31)
	dtStartTest = dt.datetime(2010,01,01)
	dtEndTest = dt.datetime(2010,12,31)
	
	''' Stack all information into one Numpy array ''' 
	naFeatTrain = ftu.stackSyms( ldfFeaturesTrain, dtStartTrain, dtEndTrain )
	naFeatTest = ftu.stackSyms( ldfFeaturesTest, dtStartTest, dtEndTest )
	
	''' Normalize features, use same normalization factors for testing data as training data '''
	ltWeights = ftu.normFeatures( naFeatTrain, -1.0, 1.0, False )
	''' Normalize query points with same weights that come from test data '''
	ftu.normQuery( naFeatTest[:,:-1], ltWeights )	
	

	lFeatures = range(0,len(lfcFeatures)-1)
	classLabelIndex = len(lfcFeatures) - 1
	
	funccall = sys.argv[1] + '(naFeatTrain,naFeatTest,lFeatures,classLabelIndex)'
	
	timestart = time.time()
	clockstart = time.clock()
	eval(funccall)
	clockend = time.clock()
	timeend = time.time()
	
	sys.stdout.write('\n\nclock diff: '+str(clockend-clockstart)+'sec\n')
	sys.stdout.write('time diff: '+str(timeend-timestart)+'sec\n')
	


