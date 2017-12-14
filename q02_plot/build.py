# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    a = sale_price.hist()
    a.axvline(x=sale_price.mean(),c= 'Red',label = 'Mean', linestyle = 'dashed')
    a.axvline(x=sale_price.median(),c= 'Black',label = 'Median',linestyle = 'dashed')
    a.axvline(x=sale_price.mode()[0],c= 'Green',label = 'Mode',linestyle = 'dashed')
    a.legend()
    plt.show()
