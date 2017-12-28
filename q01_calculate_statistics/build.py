# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here



def calculate_statistics():
    mode1=sale_price.mode()
    mode2=np.array(mode1,dtype=np.int64)
    mode=mode2[0]
    mean=sale_price.mean()
    median=sale_price.median()
    return mean,median,mode
