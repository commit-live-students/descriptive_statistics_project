# Default Imports
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    mode = stats.mode(sale_price)
    return mean,median,mode.mode[0]

# Return mean,median & mode for the SalePrice Column
# Write your code here
