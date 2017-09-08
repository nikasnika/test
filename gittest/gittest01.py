'''
Created on Sep 7, 2017

@author: I075453
'''

import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
from dtw import dtw
from sklearn.metrics.pairwise import euclidean_distances
import time
from numpy import inf
import tushare as ts
from tushare.stock.trading import get_hist_data

Series(ts.get_hist_data('000016.XSHG',start='2016-01-01',end='2016-10-01'))

