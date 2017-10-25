# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    sigma = sum((dataframe_1['SalePrice'].rank()-dataframe_2['SalePrice'].rank())**2)
    n = len(dataframe_1['SalePrice'])
    return 1 - ((6*sigma)/(n*((n**2)-1)))
