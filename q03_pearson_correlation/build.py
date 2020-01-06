# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
from scipy.stats.stats import pearsonr

# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    
    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

    return pearsonr(dataframe_1.SalePrice, dataframe_2.SalePrice)[0]


#Call to the function
correlation()



