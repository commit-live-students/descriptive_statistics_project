# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    x = dataframe_1['SalePrice'].rank() #getting ranks
    y = dataframe_2['SalePrice'].rank() #getting ranks
    d = x - y #diffrences of ranks
    #sum(d) = 0 Must!
    d_squared = d**2
    sum_of_d_squared = sum(d_squared)

    numerator = 6*sum_of_d_squared
    denominator = dataframe_1.shape[0]*((dataframe_1.shape[0]**2)-1)
    p = 1 - ((numerator)/(denominator)) #formula for spearman_correlation_coefficient


    return p
