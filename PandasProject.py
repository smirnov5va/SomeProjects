if __name__ == "__main__":
    # Write your solution here
    pass
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Graphics
data = pd.read_csv('menu.csv')
colories = data['Calories'].plot(kind='hist', bins=10, color=['red'], title='Histogram of the Calories')
fat_prot = data[['Total Fat', 'Protein']].plot(kind='box', subplots=True, title='Parallel Box Plot of the Fat and Protein')
skatt_fat_cal = data[['Total Fat', 'Calories']].plot(kind='scatter', x='Total Fat', y='Calories', title='Scatter Plot of Fat (x-axis) vs Calories + Trend Line')

#Trend line
x = data['Total Fat']
y = data['Calories']
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

plt.plot(x, p(x), 'r--')
plt.show()
