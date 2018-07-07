# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics


dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

mean=sale_price.mean()
mode=sale_price.mode()
median=sale_price.median()

# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=40)
    plt.axvline(x=mode[0],color='r')
    plt.axvline(x=median,color='b')
    plt.axvline(x=mean,color='y')
    plt.show()
    
    

plot()


