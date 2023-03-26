import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Distribution plot type

tips_info = sns.load_dataset("tips")
print(tips_info)

fig, axs = plt.subplots(ncols=7)
fig.set_size_inches(20, 5)

# 1.1 Hist plot

sns.histplot(tips_info['total_bill'], ax=axs[0])

# 1.2 KDE plot
sns.kdeplot(tips_info['total_bill'], fill=True, bw_adjust=.5, cut=0, ax=axs[1])
_ = sns.ecdfplot(tips_info['total_bill'], ax=axs[2])

sns.histplot(tips_info, x='tip', hue='sex', multiple='dodge', ax=axs[3])

# 1.3 Dis plot
sns.displot(tips_info, x='tip', hue='smoker', kind='kde', fill='True', ax=axs[4])

# 2. Regression plot type

_ = sns.regplot(x='total_bill', y='tip', data=tips_info, ax=axs[5])
_ = sns.lmplot(x='size', y='tip', data=tips_info, x_estimator=np.mean)
_ = sns.lmplot(x='total_bill', y='tip', hue='smoker', col='time', row='sex', data=tips_info)

# 3. Scatterplots

_ = sns.catplot(y='day', x='total_bill', data=tips_info)

# 3.1 swarmplot
_ = sns.catplot(y='day', x='total_bill', kind='swarm', data=tips_info)

# 3.2. violinplot
_ = sns.catplot(y='day', x='total_bill', kind='violin', hue='sex', data=tips_info)
