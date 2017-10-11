# Default Imports
import numpy as np
import pandas as pd

def calculate_statistics() :

    data = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = data.loc[:, "SalePrice"]
    print (sale_price.mean())
    print (sale_price.median())
    print (sale_price.mode())



# Return mean,median & mode for the SalePrice Column
# Write your code here
