import numpy as np
from sklearn.model_selection import KFold

data = np.arange(10)

kfold = KFold(5, shuffle=True)

for train, test in kfold.split(data):
    print('train: {}, test: {}'.format(data[train], data[test]))

    # With this loop you can split your data in training and test sets
    # Apply your algorithm for each split and evaluate with the test set!
