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
    _,args=plt.subplots(1,3)
    args[0].axvline(sale_price.mean())
    args[1].axvline(sale_price.median())
    args[2].axvline(sale_price.mode()[0])


_,args=plt.subplots(1,3)
args[0].axvline(sale_price.mean())
args[1].axvline(sale_price.median())
args[2].axvline(sale_price.mode()[0])


args[0].hist(dataframe.SalePrice)

plt.show()
dataframe
plt.ion()
plt.get_backend()


