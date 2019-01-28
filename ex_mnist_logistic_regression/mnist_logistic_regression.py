from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

# Dataset of 1797 images, each of 8x8 dimension
from sklearn.neural_network import MLPClassifier

digits = load_digits()

# check dimensionality
print("Image Data Shape: ", digits.data.shape)
print("Label Data Shape: ", digits.target.shape)

# Sets size of plot
##plt.figure(figsize=(20, 4))
##
### Visualize the data (plotting into images)
### Slightly complicated for loop to loop through first five pieces of data
##for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
##    plt.subplot(1, 5, index + 1)
##    plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
##    plt.title('Training: %i\n' % label, fontsize = 20)
##plt.show()


# Split into training and test sets to make sure after we train our
# classification algorithm, it is able to generalize well to new data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)

# Score shows the accuracy percentage
score = model.score(x_test, y_test)
print("Test set score: %f" % score)

# Printing confusion matrix
from sklearn import metrics
import seaborn as sns

cm = metrics.confusion_matrix(y_test, predictions)

##plt.figure(figsize=(9,9))
##sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
##plt.ylabel('Actual label');
##plt.xlabel('Predicted label');
##all_sample_title = 'Accuracy Score: {0}'.format(score)
##plt.title(all_sample_title, size = 15);
##plt.show()

mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=50, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.01)

mlp.fit(x_train, y_train)
print("Training set score: %f" % mlp.score(x_train, y_train))
print("Test set score: %f" % mlp.score(x_test, y_test))