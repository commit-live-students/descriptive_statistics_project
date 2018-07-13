import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def plot():
    t=calculate_statistics()
    sale_price.hist()
    plt.axvline(t[0], color='b', linestyle='solid', linewidth=2)
    plt.axvline(t[1], color='r', linestyle='dashed', linewidth=4)
    plt.axvline(t[2], color='1', linestyle='dotted', linewidth=2)
    plt.show()
