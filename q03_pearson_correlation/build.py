# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'))
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
house_price = dataframe_1.loc[:, 'SalePrice']

dataframe_2 = pd.read_csv('data/house_prices_copy.csv').loc[:, 'SalePrice']
weight_of_nasa_space_shuttle = dataframe_2.loc[:, 'SalePrice']

# Return the correlation value between the SalePrice column for the two loaded datasets