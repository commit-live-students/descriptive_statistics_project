# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
import statistics as st

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']

def calculate_statistics():
    
    mean = sale_price.mean()
    median = sale_price.median()
    mode = st.mode(sale_price)
    
    return mean, median, mode

a,b,c = calculate_statistics()








