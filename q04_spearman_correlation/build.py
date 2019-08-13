import numpy as np
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

#Convert the series into dataframe usinf to_frame() function
X = dataframe_1['SalePrice'].to_frame()
Y = dataframe_2['SalePrice'].to_frame()

#merge the two dataframes (saleprice) and perform spearman_correlation to get the co-efficient
#Return the value of the dataframe(2*2 dataframe) output created while calculating the co-efficient
def spearman_correlation():
    value = pd.merge(X,Y,left_index=True, right_index=True).corr(method='spearman')
    return float(value.loc['SalePrice_y']['SalePrice_x'])
