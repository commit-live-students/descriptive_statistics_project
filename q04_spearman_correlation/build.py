# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    df1 = pd.DataFrame(data=dataframe_1, columns=['SalePrice'])
    df1.rename(columns={'SalePrice':'df1SP'}, inplace=True)
    df2 = pd.DataFrame(data=dataframe_2, columns=['SalePrice'])
    df2.rename(columns={'SalePrice':'df2SP'}, inplace=True)
    df3 = df1.merge(df2, left_index=True, right_index=True)
    df4 = df3.corr(method='spearman')
    return float(df4.loc['df1SP','df2SP'])

#print spearman_correlation()
