# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('../data/house_prices_multivariate.csv')
house_price = dataframe_1.loc[:, 'SalePrice']

dataframe_2 = pd.read_csv('../data/house_prices_copy.csv')
weight_of_nasa_space_shuttle = dataframe_2.loc[:, 'SalePrice']

# Write your code here
# Create a function spearman_correlation() that returns the Spearman Correlation Coeffecient between the two loaded columns