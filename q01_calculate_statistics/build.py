# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    med = float(np.median(sale_price))
    mod = np.int64(np.array(stats.mode(sale_price)[0][0]))
    return np.mean(sale_price), med, mod

print calculate_statistics()
