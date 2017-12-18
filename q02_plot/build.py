import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    #Get the mean, median and mode from calculate_statistics function for saleprice for housing Iowa
    args=calculate_statistics()

    #figure(figsize=(1,1)) creates an inch-by-inch image, which will be 80-by-80 pixels unless you also give a different dpi argument.
    plt.figure(figsize=(10, 6))

    #plot the histogram for sale_price {bins = range of values on x axis and y denotes the count of elements falling between those range}
    plt.hist(sale_price, bins=40)

    #plot the mean by value on x being mode/mean/median plotted 300 times while on y being plotted 0-299 times to get a straight line
    plt.plot([args[0]]*300, range(300), label='mode')
    plt.plot([args[1]]*300, range(300), label='median')
    plt.plot([args[2]]*300, range(300), label='mean')

    #limit the length of y till 250 only
    plt.ylim(0, 250)

    #plot the lables as well defined in mean, median and mode plotting
    plt.legend()

    #finally show the histogram along with mean, median and mode
    plt.show
