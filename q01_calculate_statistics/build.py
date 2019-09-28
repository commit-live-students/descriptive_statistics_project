# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    ar = np.array(sale_price)
    mode1 = np.bincount(ar)
    mode = np.argmax(mode1)
    return mean, median, mode
