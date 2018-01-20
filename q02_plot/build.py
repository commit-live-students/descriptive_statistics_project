import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset

def plot():
    mean1 = sale_price.mean()
    median1 = sale_price.median()
    mode1 = sale_price.mode()
    #mod = np.int64(np.array(mode1))

    plt.hist(sale_price)
    plt.axvline((mode1), ls ='dashed', label='mode', c= 'red')
    plt.axvline((median1), ls = 'dashed', label='median', c= 'blue')
    plt.axvline((mean1), ls= 'dashed', label='mean', c = 'green')
    plt.axvline(int(sale_price.mode()),ls = 'dashed', c = 'blue')
    plt.show()
