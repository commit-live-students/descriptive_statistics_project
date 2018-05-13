# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    #print(dataframe_1.info())
    #print(dataframe_2.info())
    #df1SalePrice = dataframe_1['SalePrice']
    #df2SalePrice = dataframe_2['SalePrice']
    finalDF = pd.DataFrame({'SalePrice1': dataframe_1['SalePrice'],'SalePrice2':dataframe_2['SalePrice']})
    #print(type(df1SalePrice))
    finalDF['Rank1'] = finalDF['SalePrice1'].rank(ascending = True ,method ='first')
    finalDF['Rank2'] = finalDF['SalePrice2'].rank(ascending = True ,method ='first')
    finalDF['d'] = finalDF['Rank1'] - finalDF['Rank2']
    finalDF['d-squared'] = finalDF['d'] ** 2
    dfSum = finalDF['d-squared'].sum()
    print(dfSum)
    spearmanCon = 1 - ( (6 * dfSum) /  (finalDF.shape[0] *( finalDF.shape[0] ** 2 +1)))
    print(spearmanCon)
    return spearmanCon
spearman_correlation()


