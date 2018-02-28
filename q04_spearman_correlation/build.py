# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
	dataframe_1['rank1'] = dataframe_1['SalePrice'].rank(ascending=True)
	dataframe_2['rank2'] = dataframe_2['SalePrice'].rank(ascending=True)
	dataframe_1['d'] = dataframe_1['rank1'].subtract(dataframe_2['rank2'])
	dataframe_1['d_square'] = dataframe_1['d'] ** 2
	sample_size = dataframe_1.shape[0]
	# spearman correlation formula is
	# 1 - (6 * sum (d_square) / ((sample_size ** 3) - sample_size) )
	sp_coeff = 1 -  ( (6 * dataframe_1['d_square'].sum() ) / ((sample_size ** 3) - sample_size) )
	sp_coeff1 = dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'],method='spearman')
	print "\nAlternate method : ", sp_coeff1
	return sp_coeff1
