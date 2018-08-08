# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')

# Draw the plot for the mean, median and mode for the dataset
def plot():
    df=pd.DataFrame(dataframe)
    sale_price = df['SalePrice']
    a=sale_price.mean()
    b=sale_price.median()
    c=sale_price.mode()[0]
    plt.hist('SalePrice',bins=10)
    plt.axvline(a,color='w',linestyle='dashed',linewidth=2)
    plt.axvline(b,color='r',linestyle='dashed',linewidth=2)
    plt.axvline(c,color='b',linestyle='dashed',linewidth=2)
    plt.show()
c=plot()
c


