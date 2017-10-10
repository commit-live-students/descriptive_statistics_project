# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    sale_price_mean=sale_price.mean()
    sale_price_median=np.median(sale_price).item()
    #.astype('float')
    sale_price_mode=sale_price.mode()
    return(sale_price_mean,sale_price_median,sale_price_mode[0])



#(mean, float, "Expected data type for mean is float you are returning %s" % (type(mean)))
#(median, float, "Expected data type for median is float you are returning %s" % (type(median)))
#(mode, numpy.int64, "Expected data type for mode is numpy.int64 you are returning %s" % (type(mode)))
