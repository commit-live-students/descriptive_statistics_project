# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
def plot():
    mean=sale_price.mean()
    median=sale_price.median()
    mode=np.array(sale_price.mode(), dtype=np.int64)[0]
    plt.hist(sale_price,bins=60)
    plt.axvline(x=mean, color='r',linewidth=2,label='Mean')
    plt.axvline(x=median, color='g',linewidth=2, label='Median')
    plt.axvline(x=mode, color='y',linewidth=2, label='Mode')
    plt.legend()
    plt.show()





