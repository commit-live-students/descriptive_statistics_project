import sys
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('Agg') 

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean=sale_price.mean()
    median=sale_price.median()
    mode=sale_price.mode()
    plt.figure(figsize=(10,6))
    plt.hist(sale_price,bins=60)
    plt.axvline(x=mean)
    plt.axvline(x=median)
    plt.axvline(x=mode.item())
    plt.show()
    
plot()



