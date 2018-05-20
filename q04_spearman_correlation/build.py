# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    # DataFrame.corr(method='pearson', min_periods=1)
    # method : {âpearsonâ, âkendallâ, âspearmanâ}
    df = pd.DataFrame(data=dataframe_1.SalePrice)
    df['S2'] = dataframe_2.SalePrice
    r = df.corr(method='spearman')
    return r.iloc[0,1]
spearman_correlation()


