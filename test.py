# creating a neural network
import numpy as np
from numpy.f2py.auxfuncs import process_f2cmap_dict

np.random.seed(42)
x = np.random.randn(5, 6)  # 5 rows and 6 columns. 5 rows means 5 examples
w1 = np.random.randn(
    6, 4
)  # since there are 6 features per row therefore w1 will have 6 rows. 1 weight for each feature.
w2 = np.random.randn(
    4, 3
)  # the output of first layer will be 4 units. Therefore the next layer will receive 4 examples.
w3 = np.random.randn(3, 1)
b1 = np.random.randn(
    4,
)  # because there are 4 units of the first layer so each unit would need a bias.
b2 = np.random.randn(
    3,
)  # because there are 3 units of the second layer so each unit would require a bias.
b3 = np.random.randn(
    1,
)  # because the output layer has 1 unit only therefore there will be requirement of 1 bias.
y = np.random.randn(
    5,
)  # 5 rows means, 1 y for each example.


def relu(z):
    return np.maximum(0, z)


def sigmoid(z):
    return 1 / (
        1 + np.exp(-z)
    )  # to get the output between 0 and 1. This is the level of prediction.


def dense(x, w, b, activation=""):
    z = np.matmul(x, w) + b
    if activation == "relu":
        return relu(z)
    else:
        return sigmoid(z)


def sequential(x, w1, b1, w2, b2, w3, b3):
    a1 = dense(x, w1, b1, activation="relu")
    a2 = dense(a1, w2, b2, activation="relu")
    a3 = dense(a2, w3, b3, activation="sigmoid")
    return a3


a3 = sequential(x, w1, b1, w2, b2, w3, b3)

predictions = np.zeros_like(a3)

for i in range(len(a3)):
    if a3[i] >= 0.5:
        predictions[i] = 1
    else:
        predictions[i] = 0
print(a3)
print(predictions)
