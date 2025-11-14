import numpy as np


#performing sigmoid operation
def sigmoid(z):
    return 1/(1 + np.exp(-z))

#performing layer operation
def dense(x,w,b):
    z = np.matmul(x,w) + b #performed matrix multiplication here with numpy's vectorization feature
    a_out = sigmoid(z) #applying sigmoid to get an output between 0-1
    return a_out

def sequential(x,w1,b1,w2,b2,w3,b3):
    a1 = dense(x,w1,b1)
    a2 = dense(a1,w2,b2)
    a3 = dense(a2,w3,b3)
    return a3

np.random.seed(42)
x = np.random.randn(5,4)

#since we want layer 1 to have 6 neurons
w1 = np.random.randn(4,6) #since the x has 4 columns which means 4 features so w1 must have 4 rows each for each feature of x. 6 means there will be 6 neurons
b1 = np.random.randn(6,) #defining bias for each of the 6 neurons.

w2 = np.random.randn(6,3)
b2 = np.random.randn(3,)

w3 = np.random.randn(3,1)
b3 = np.random.randn(1,)

output = sequential(x, w1,b1,w2,b2,w3,b3)
print(f"Input Shape: ", x.shape)
print(f"Output Shape: ", output.shape)
print(f"Predictions: \n", output)

#output after applying predictions
yhat = np.zeros_like(output)
for i in range(len(yhat)):
    if output[i] >= 0.5:
        yhat[i] = 1
    else:
        yhat[i] = 0
print(f"yhat: \n{yhat}")

print("Done!")