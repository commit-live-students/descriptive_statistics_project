# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean_sale = np.mean(sale_price)
    median_sale = np.median(sale_price)
    mode_sale = sale_price.mode()
    return mean_sale, median_sale, mode_sale[0]
