import numpy as np
import matplotlib.pyplot as plt

x = np.arange(50)

y_line = x + 10 * np.random.rand(50)

y_curve = x**2 + 25 * np.random.rand(50)

# plt.scatter(x, y_line)
# plt.show()
#
# plt.scatter(x, y_curve)
# plt.show()

x = x.reshape(-1, 1)

from sklearn.linear_model import LinearRegression, Ridge, Lasso

lr = LinearRegression().fit(x, y_line)
lr_model_plot = lr.predict(x)
print(f'Linear Regression R^2 Score: {lr.score(x, y_line)}')

ridge = Ridge(alpha=0.5).fit(x, y_line)
ridge_model_plot = ridge.predict(x)
print(f'Ridge R^2 Score:  {ridge.score(x, y_line)}')

lasso = Lasso(alpha=0.5).fit(x, y_line)
lasso_model_plot = lasso.predict(x)
print(f'Lasso R^2 Score: {lasso.score(x, y_line)}')

# plt.plot(lr_model_plot)
# plt.plot(ridge_model_plot)
# plt.plot(lasso_model_plot)
# plt.scatter(x, y_line)
# plt.show()


lr = LinearRegression().fit(x, y_curve)
lr_model_plot = lr.predict(x)
print(f'Linear Regression R^2 Score: {lr.score(x, y_curve)}')

ridge = Ridge(alpha=2).fit(x, y_curve)
ridge_model_plot = ridge.predict(x)
print(f'Ridge R^2 Score:  {ridge.score(x, y_curve)}')

lasso = Lasso(alpha=2).fit(x, y_curve)
lasso_model_plot = lasso.predict(x)
print(f'Lasso R^2 Score: {lasso.score(x, y_curve)}')

plt.plot(lr_model_plot)
plt.plot(ridge_model_plot)
plt.plot(lasso_model_plot)
plt.scatter(x, y_curve)
plt.show()



