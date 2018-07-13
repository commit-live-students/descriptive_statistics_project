import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    dataframe_1['Rank'] = dataframe_1['SalePrice'].rank(ascending=1)
    dataframe_2['Rank'] = dataframe_2['SalePrice'].rank(ascending=1)
    dataframe_1['d']=dataframe_1['Rank']-dataframe_2['Rank']
    dataframe_1['d2']=dataframe_1['d']**2
    D1=dataframe_1['d2'].sum()
    D2=D1*6
    n=dataframe_1.shape[0]
    m=(n**2)-1
    s=1-(D2/(n*m))
    return s
