# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
from inspect import getfullargspec

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean,median,mode=calculate_statistics()
    #plt.hist(sale_price)
    plt.axvline(x=mean,c='r')
    plt.axvline(x=median,c='y')
    plt.axvline(x=mode,c='g')
    plt.show()
    
plot()




