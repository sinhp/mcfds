import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# Generate some example data
x, y = make_classification(n_samples=1000, n_features=10, n_informative=5,
                            n_redundant=0, n_classes=2, random_state=42)

# Create Training and Testing Data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the Logistic-CEM model
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x_train, y_train)

# Predict labels for the test data
y_pred = model.predict(x_test[:,:-1])

# Compute accuracy of the predictions
acc = accuracy_score(y_test, y_pred)

print(f"Accuracy: {acc}")
print("Predicted labels:")
print(y_pred)