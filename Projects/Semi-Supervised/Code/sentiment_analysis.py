import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from datasets import load_dataset

# load the IMDB dataset from the datasets library, this is a binary classification dataset with 50k training and 50k test examples
imdb = load_dataset("imdb")


def sstc(train_data, test_data, train_labels, test_labels):
    '''
    This function trains a logistic regression model on the IMDB dataset and prints the accuracy on the test set using scikit-learn (LogisticRegression)
        Parameters:
            train_data (list): list of strings, each string is a review from the training set
            test_data (list): list of strings, each string is a review from the test set
            train_labels (list): list of integers, each integer is the label (0 or 1) for the corresponding review in train_data
            test_labels (list): list of integers, each integer is the label (0 or 1) for the corresponding review in test_data
    '''
    # create a vectorizer object to generate feature vectors, we will use word counts as features
    vectorization = CountVectorizer()
    X_train = vectorization.fit_transform(train_data)
    X_test = vectorization.transform(test_data)

    # train a logistic regression model on the training set
    model = LogisticRegression(random_state=0).fit(
        X_train, train_labels)

    # make predictions on the test data
    y_pred = model.predict(X_test)

    return np.mean(y_pred == test_labels), y_pred


# create a list of training set sizes to iterate over, we will use 1k, 10k, and 50k examples.
# You will notice that as the training set size increases, the accuracy increases.
size = [1000, 10000, 25000]
results = []
for i in size:
    train_set = imdb["train"].shuffle(seed=42).select(
        [i for i in list(range(i))])
    test_set = imdb["test"].shuffle(seed=42).select(
        [i for i in list(range(i))])

    # split the data into text and labels
    train_data = train_set["text"]
    test_data = test_set["text"]
    train_labels = train_set["label"]
    test_labels = test_set["label"]

    # convert the labels to numpy arrays for use with scikit-learn
    y_train = np.array(train_labels)
    y_test = np.array(test_labels)
    results.append(sstc(train_data, test_data, y_train, y_test))

for i in range(len(size)):
    print("Accuracy on test set with {} training examples: {}".format(
        size[i], results[i][0]))
    print("Predictions on test set with {} training examples: {}".format(
        size[i], results[i][1][0:10])
    )

# Accuracy on test set with 1000 training examples: 0.789
# Predictions on test set with 1000 training examples: [1 0 0 1 0 1 0 0 0 0]
# Accuracy on test set with 10000 training examples: 0.8593
# Predictions on test set with 10000 training examples: [1 0 1 1 0 1 0 0 1 1]
# Accuracy on test set with 25000 training examples: 0.86396
# Predictions on test set with 25000 training examples: [1 0 1 1 0 0 0 0 0 1]
