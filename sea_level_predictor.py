import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Import data
df = pd.read_csv('epa-sea-level.csv')
modified_df = df[df['Year'] >= 2000]

# Setting variables
x = df['Year']
y = df['CSIRO Adjusted Sea Level']

mod_x = modified_df['Year']
mod_y = modified_df['CSIRO Adjusted Sea Level']

# Setting up plot
fig, ax = plt.subplots()

ax.set_title('Rise in Sea Level')
ax.set_xlabel('Year')
ax.set_ylabel('Sea Level (inches)')

# Plotting data

## Scatter plot
scatter_plot = sns.scatterplot(data=df, x=x, y=y, hue=y, palette='Blues')

## Line plots
lr_1 = linregress(x, y)
lr_2 = linregress(mod_x, mod_y)

years = np.arange(1880, 2051)
mod_years = np.arange(2000, 2051)

y_pred1 = [lr_1.slope * xi + lr_1.intercept for xi in years]
y_pred2 = [lr_2.slope * xi + lr_2.intercept for xi in mod_years]

l1 = sns.lineplot(x=years, y=y_pred1, label='Prediction: 1880 -> 2050')
l2 = sns.lineplot(x=mod_years, y=y_pred2, label='Prediction: 2000 -> 2050')

ax.legend(title='CSIRO Adjusted Sea Level', fontsize='small')
plt.show()