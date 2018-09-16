# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(sale_price)
    mean=sale_price.mean()
    median=sale_price.median()
    mode=sale_price.mode()[0]
    plt.axvline(mean, linewidth=1, color='r', linestyle='dashed')
    plt.axvline(median, linewidth=1, color='y', linestyle='dashed')
    plt.axvline(mode, linewidth=1, color='b') 
    plt.show()
    
plot()




