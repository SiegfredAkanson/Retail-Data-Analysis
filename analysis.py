import numpy as np
import pandas as pd

#Part 2 : Numpy
np.random.seed(42)
sales = np.random.normal(loc=5000, scale=1000, size=365)

mean = np.mean(sales)
std = np.std(sales)

surge_days = sales > (mean+1.5*std)
labels = np.where(surge_days, "High", "Normal")
print(labels[:10])
