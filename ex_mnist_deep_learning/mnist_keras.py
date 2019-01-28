from keras.datasets import mnist
import matplotlib.pyplot as plt

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

### plot 4 images as gray scale
##plt.subplot(221)
##plt.imshow(X_train[0], cmap=plt.get_cmap('gray'))
##plt.subplot(222)
##plt.imshow(X_train[1], cmap=plt.get_cmap('gray'))
##plt.subplot(223)
##plt.imshow(X_train[2], cmap=plt.get_cmap('gray'))
##plt.subplot(224)
##plt.imshow(X_train[3], cmap=plt.get_cmap('gray'))
### show the plot
##plt.show()

# Load keras essentials
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils

# We will be using a simple multi-layer perceptron model
# In this case, we have to flatten the input data into a vector of pixels
# In this case the 28x28 sized images will be 784 pixel input values
num_pixels = X_train.shape[1] * X_train.shape[2]

X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')

# The pixel values are gray scale between 0 and 255. For neural networks,
# it is usually a good idea to perform some scaling. Overly large and small
# values tend to lead to some performance issues. The recommended scale is
# between 0 and 1. Since we know the range is 0-255, we can easily scale it
# by dividing throught by 255.
X_train = X_train /255
X_test = X_test / 255

# Now let us look at the labels (y_train, y_test)
# They represent the digits
# But our problem here is categorization
# there is actually no numerical relationship between the numbers
# They are actually categories!
# Can anyone remember what we did earlier to transform categorical variables?
# Yup! We do one hot encoding.
# We can do this using keras np_utils
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

# Build our model
# This defines the structure of it
# What we are doing below is a simple 2 layer model, with 300 nodes in first layer, and 10 nodes in second layer
# Check out keras documentation to learn about all the details
model = Sequential()
model.add(Dense(300, input_dim=num_pixels, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# call the fit function
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)

# We can plot the history
print(history.history.keys())

# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
