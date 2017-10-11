import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    x=dataframe_1['SalePrice']
    y=dataframe_2['SalePrice']
    a=x.rank(ascending=1)
    b=y.rank(ascending=1)
    c=(a-b)**2
    n=len(c)
    di=c.sum()
    D=n**3 - n
    N=6*di
    X=N/D
    return 1-X
