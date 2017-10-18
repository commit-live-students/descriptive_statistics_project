# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]
def calculate_statistics():
    a=np.mean(sale_price)
    b=float(np.median(sale_price))
    x=sale_price.value_counts()
    d=np.int64(np.asscalar(x[x.values==x.values.max()].index))
    return a,b,d
