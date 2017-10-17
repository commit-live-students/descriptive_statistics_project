# Default Imports
import pandas as pd
import scipy.stats
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def correlation():
    Pr_coef = dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'], method='pearson', min_periods=None)
    return Pr_coef
    # Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
correlation()

# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
