# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    data = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = data.loc[:, 'SalePrice']
    df_mean= float(sale_price.mean())
    df_median= float(sale_price.median())
    df_mode=sale_price.astype(np.int64).mode()
    return df_mean, df_median, df_mode[0]
    


