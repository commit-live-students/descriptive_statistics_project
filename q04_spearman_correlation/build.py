# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    df = pd.DataFrame()
    df["sp1"] = dataframe_1["SalePrice"]
    df["sp2"] = dataframe_2["SalePrice"]
    cor = df.corr(method="spearman")
    return cor.loc["sp1"][1]
