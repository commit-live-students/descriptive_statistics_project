# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    mean_sales_price = sale_price.mean()
    median_sales_price = sale_price.median()
    mode_sales_price = sale_price.mode()[0]



    print(mean_sales_price,median_sales_price,mode_sales_price)

calculate_statistics()
