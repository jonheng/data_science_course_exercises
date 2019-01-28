from sklearn import datasets

boston = datasets.load_boston()

# This data is similar to a dictionary
# Contains 4 keys
# 1. data: data for all the features
# 2. feature_names: column names
# 3. DESCR: a description of the dataset
# 4. target: the dependent variable/MEDV/median home value in thousands

boston.keys()

# You can read its description by printing the following
print(boston.DESCR)

# Let's load this into something we are more familiar with, the pandas dataframe
import numpy as np
import pandas as pd

x = pd.DataFrame(boston.data, columns=boston.feature_names)

y = pd.DataFrame(boston.target, columns=["MEDV"])

print(x.head())

print(y.head())

# Let us now use the sklearn linear regression model
from sklearn import linear_model

lm = linear_model.LinearRegression()
model = lm.fit(x, y)

predictions = lm.predict(x)

# We can look at how well our model fit
# R^2 is calculated through using the residual sum of squares
# The best value is 1 and worst is
print('OLS R^2 Score: ',lm.score(x, y))

# ridge
for alpha in [0.1, 0.5, 1.0, 1.5, 2.0]:
    ridge = linear_model.Ridge(alpha).fit(x, y)
    print('Alpha: ', alpha)
    print('Ridge R^2 Score:', ridge.score(x, y))
    # print(ridge.coef_)

# We can also check the values of the parameters of the model
print(lm.coef_)
print(lm.intercept_)


# We can look at how well the predictions are graphically
pred_df = pd.DataFrame(predictions)
concat_df = pd.concat([y, pred_df], axis='columns')

import matplotlib.pyplot as plt

plt.plot(concat_df[:50])
plt.show()

# We are unable to visualize it nicely on a 2D graph, since the dataset is
# actually multi dimensional. The nice 2D linear regression graphs
# you find in the slides are when there is a single x variable.
# Here we have up to around 13.
