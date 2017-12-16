# Default Imports
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    Sales_price = pd.Series(data['SalePrice'])
    mean = Sales_price.mean()
    median = Sales_price.median()
    mode = np.array(Sales_price.mode(),dtype=np.int64)
    return mean, median, mode[0]
