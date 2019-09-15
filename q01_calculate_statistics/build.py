# Default Imports
import numpy as np
import pandas as pd
import scipy.stats

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean_sale = sale_price.mean()
    median_sale = sale_price.median()
    mode_sale = sale_price.mode()
    np_type = np.dtype('int64').type(mode_sale)

    return mean_sale, median_sale, np_type

print calculate_statistics()
