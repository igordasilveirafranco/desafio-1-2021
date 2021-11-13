import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

account = pd.read_csv("assets\data\ACCOUNTS.csv")
mylist = account.dropna()
type(mylist)
# mylist = np.random.randn(10, 1000).cumsum(axis=1).ravel() / 500
# step = 0.01
# start = np.floor(min(mylist) / step) * step
# stop = max(mylist) + step
# bin_edges = np.arange(start, stop, step=step)
# plt.hist(mylist, bins=bin_edges, color='crimson', ec='white')
# plt.xticks(bin_edges, rotation=90)
# plt.tight_layout()
# plt.show()
