# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

# Return mean,median & mode for the SalePrice Column
def calculate_statistics():
    mean=sale_price.mean()
    median=sale_price.median()
    mode=sale_price.mode()[0]
    return(mean,median,mode)

calculate_statistics()
