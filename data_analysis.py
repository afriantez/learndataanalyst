import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv("sales_data.csv")

# show 5 first row
print(df.head())
# show data type
print(df.info())
# summary statistics
print(df.describe())
# show summary missing value
# print(df.isnull().sum())

# data cleaning
# if df.isnull().values.any():
#    df.fillna(0, inplace=True)

# top 5 selling product
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5))

# show revenue over year
#plt.figure(figsize= (10, 5))
#sns.lineplot(x= "Date", y= "Revenue", data= df)
#plt.title("Revenue over year")
#plt.show