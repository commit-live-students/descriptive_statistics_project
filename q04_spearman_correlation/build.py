# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
sale_price1 = pd.DataFrame(dataframe_1.loc[:, "SalePrice"])
sale_price1['Rank1'] = sale_price1['SalePrice'].rank(ascending=False)
sale_price2 = pd.DataFrame(dataframe_2.loc[:, "SalePrice"])
sale_price2['Rank2'] = sale_price2['SalePrice'].rank(ascending=False)
dataframe = pd.merge(sale_price1, sale_price2, left_index=True, right_index=True)
dataframe['Diff'] = dataframe['Rank1'] - dataframe['Rank2']
dataframe['Diff_sqr'] = dataframe['Diff'] ** 2
#print dataframe
# Your code here
def spearman_correlation():
    sum_diff_sqr = dataframe['Diff_sqr'].sum()

    spearman_correlation_coeff = 1- ((6 * sum_diff_sqr) / (1379 * ((1379 ** 2) - 1)))

    return spearman_correlation_coeff
print spearman_correlation()
