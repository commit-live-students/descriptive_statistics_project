# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics


dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    mean1=sale_price.mean()

    median1 = sale_price.median()

    mode1 = sale_price.mode()[0]

    plt.hist(sale_price.values)
    plt.axvline(mean1,color="r")
    plt.axvline(median1,color="y")
    plt.axvline(mode1,color="g")
    plt.title("sales price distribution")
