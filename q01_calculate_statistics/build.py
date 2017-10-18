# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def calculate_statistics():
    Sales_price = pd.Series(data['SalePrice'])
    mean = np.mean(Sales_price)
    median = np.median(Sales_price)
    mode = Sales_price.mode()
    return mean,median,mode[0]

calculate_statistics()
