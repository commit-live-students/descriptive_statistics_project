# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('./data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('./data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    #df = pd.DataFrame()
    sp1 = dataframe_1.loc[:,'SalePrice'].sort_values()
    sp2 = dataframe_2.loc[:,'SalePrice'].sort_values()
    df_cal = pd.DataFrame()
    df_cal['sp1'] = sp1
    df_cal['sp2'] = sp2
    #df['d'] = sp1 - sp2
    #df['d-squared'] = (sp1 - sp2) ** 2
    #d_sqr_sum = df['d-squared'].sum()
    #n = df.shape[0]
    #print (df['d-squared'].tail())
    #print (d_sqr_sum)
    #print (n)
    #s_corr = 1 - (6 * d_sqr_sum / (n * (n ** 2 - 1)))
    #print (s_corr)
    return (float(df_cal.corr(method='spearman').iloc[0,1]))
#print (type(spearman_correlation()))
