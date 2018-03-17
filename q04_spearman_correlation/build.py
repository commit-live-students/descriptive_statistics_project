# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    dataframe_1["rank"] = dataframe_1.SalePrice.rank(ascending=1)
    dataframe_2["rank"] = dataframe_2.SalePrice.rank(ascending=1)

    dataframe_1["d"] = dataframe_1["rank"] - dataframe_2["rank"]
    dataframe_1["dsquared"] = dataframe_1["d"] **2

    return 1 - ((dataframe_1["dsquared"].sum() *6 ) / (dataframe_1["dsquared"].shape[0]*(dataframe_1["dsquared"].shape[0]**2-1)))
