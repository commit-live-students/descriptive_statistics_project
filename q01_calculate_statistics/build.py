# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    return np.mean(sale_price),float(np.median(sale_price)),sale_price.mode()[0]


mean, median, mode = calculate_statistics()
type(mode)


