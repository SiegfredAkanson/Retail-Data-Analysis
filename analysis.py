import numpy as np
import pandas as pd
from pandas._config import dates

#Part 2 : Numpy
np.random.seed(42)
sales = np.random.normal(loc=5000, scale=1000, size=365)

mean = np.mean(sales)
std = np.std(sales)

surge_days = sales > (mean+1.5*std)
labels = np.where(surge_days, "High", "Normal")
print(labels[:10])

#Part 2: Pandas
dates = pd.date_range(start="2025-01-01", periods=365) #creating dataframes
df = pd.DataFrame({"Date":dates, "Sales":sales})

df["Rev_after_tax"] = df["Sales"]*0.85 #Revenue after tax
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum() #Monthly Total Sales
print(monthly_sales)

