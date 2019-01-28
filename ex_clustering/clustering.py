from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = datasets.load_iris()

##print(iris.keys())
##
##print(iris.DESCR)
##
##print(iris.feature_names)
##
##print(iris.target)
##
##print(iris.target_names)


# Slicing dataset
# This takes the all rows, first column
# First column corresponds to the sepal length (check feature_names)
x_axis = iris.data[:, 0]  # Sepal length
y_axis = iris.data[:, 1]  # Sepal width

# Scatter plot
# Check https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html
# for documentation
##plt.scatter(x_axis, y_axis, c=iris.target)
##plt.show()
      



df = pd.DataFrame(iris.data, columns=iris.feature_names)

variable_names = df.columns

df['target'] = iris.target

# Shows some summary statistics 
df.describe()

##g = sns.pairplot(df, hue='target', vars=variable_names)

# Display it by typing plt.show()

### K means clustering ###
from sklearn.cluster import KMeans

# Model
model = KMeans(n_clusters=3)

# Model Fitting
model.fit(iris.data)

predictions = model.predict(iris.data)

print(predictions)
print(iris.target)

df['predictions'] = predictions

sns.pairplot(df, hue='predictions', vars=variable_names)
plt.show()

### Hierarchical clustering ###
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

# Perform hierarchical clustering
# Method defines the distance metric used
# Check documentation for other types

##complete = linkage(iris.data, method='complete')
##
##d1 = dendrogram(complete, labels=iris.target, color_threshold=3.5)

ward = linkage(iris.data, method='ward')

d2 = dendrogram(ward, labels=iris.target, color_threshold=7.0)

cluster_labels = fcluster(ward, 3, criterion='maxclust')

df['predictions'] = predictions

g1 = sns.pairplot(df, hue='predictions', vars=variable_names)
g2 = sns.pairplot(df, hue='target', vars=variable_names)
