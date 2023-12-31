import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv('honeyproduction.csv')

prod_per_year = df.groupby('year').totalprod.mean().reset_index()
X = prod_per_year['year']
X = X.values.reshape(-1, 1)
y = prod_per_year['totalprod']

regr = linear_model.LinearRegression()
regr.fit(X, y)
y_predict = regr.predict(X)

X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)
future_predict = regr.predict(X_future)

plt.scatter(X, y)
plt.plot(X, y_predict)
plt.plot(X_future, future_predict)
plt.savefig('honey_future.png')
plt.show()

print(df.head())
print(regr.coef_)
print(regr.intercept_)
