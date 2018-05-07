# Default Import
import scipy.stats
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
dataframe_1.head



#df['rank_l']=df['SalePrice_l'].rank(axis=0,method='min')
#df['rank_r']=df['SalePrice_r'].rank(axis=0,method='min')
#df['rankdiff']=df['rank_l']-df['rank_r']
#df['rankdiffsquare']=df['rankdiff']*df['rankdiff']

#sumd=sum(df['rankdiffsquare'])
#print(sumd)

#pear=1-((6*sumd)/(n*(n*n-1)))
#print(pear)
#df.head()
def spearman_correlation():
    df=dataframe_1.join(dataframe_2,lsuffix='_l',rsuffix='_r')
    r=scipy.stats.spearmanr(df['SalePrice_l'],df['SalePrice_r'])
    r=float(r[0])
    return(r)



r=spearman_correlation()
r

