# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    x1 = pd.DataFrame(dataframe_1['SalePrice'])
    x2 = pd.DataFrame(dataframe_2['SalePrice'])

    x1['Rank'] = x1['SalePrice'].rank(ascending = False)
    x2['Rank'] = x2['SalePrice'].rank(ascending = False)

    dsq = (x1['Rank'] - x2['Rank'])**2
    n = dsq.shape[0]
    num = float(6*sum(dsq))
    den = float(n*(n**2-1))
    return (1 - num/den)
