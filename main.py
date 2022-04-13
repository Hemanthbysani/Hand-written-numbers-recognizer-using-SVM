# initializing the libraries
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# loading the data from sklearn's database
img_digits = datasets.load_digits()

# showing the training set data
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, img_digits.images, img_digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)

num_samples = len(img_digits.images)
data = img_digits.images.reshape((num_samples, -1))

classifier = svm.SVC(gamma=0.001)
# data splitting for training and comparision
# randomized the data with shuffle and a random seed of 1
X_train, X_test, y_train, y_test = train_test_split(data, img_digits.target, test_size=0.4, shuffle=True, random_state=1)

# fitting the model
classifier.fit(X_train, y_train)

# predicting the values using the fitted model
predicted_val = classifier.predict(X_test)

# showing predicted values and their supplied values by resizing anf flattening the image
_, axis = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for xes, image, predictions in zip(axis, X_test, predicted_val):
    xes.set_axis_off()
    image = image.reshape(8, 8)
    xes.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    xes.set_title(f"Prediction's : {predictions}")

# generating the report using sklearn's classification_report
print(
    f"Classification report for {classifier}:\n"
    f"{metrics.classification_report(y_test, predicted_val)}\n"
)

# generating the confusion matrix
disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted_val)
disp.figure_.suptitle("Confusion matrix")
print(f"Confusion matrix: \n{disp.confusion_matrix}")

plt.show()