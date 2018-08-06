# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


#def plot():
   # cc = sale_price.mean(), sale_price.median(), sale_price.mode().iloc[0]
    #xvline(linewidth=4, color='r')
def plot():
    plt.axvline(sale_price.mean())
    plt.axvline(sale_price.median())
    plt.axvline(sale_price.mode()[0])
    plt.hist(sale_price, bins=10)
    
plot()
    

#plot()


# Draw the plot for the mean, median and mode for the dataset





