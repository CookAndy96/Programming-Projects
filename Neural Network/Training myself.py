import numpy as np

'''This is coding practice taken from the amazing tutorial found here https://iamtrask.github.io/2015/07/12/basic-python-network/. I added my own comments to further explain the parts for myself.'''

# Initilise sigmoid function. The sigmoid function takes a dataset as input and outputs values between 1 and 0.
def sigmoid(x, deriv = False):
    if deriv == True:
        return np.multiply(x,(1-x))     # Return the derivative of the sigmoid function
    return np.divide(1,(1+np.exp(-x)))   # Return sigmoid function

# Input dataset
x   = np.array([[0,0,1],    #Data organised as a matrix with each row corresponding to one value in the output y.
               [0,1,1],
               [1,0,1],
               [1,1,1]])

# Output data
y   = np.array([[0,0,1,1]]).T   #Changes a 1,4 matrix to a 4,1 matrix that can be assigned as the outputs in x.

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)
 
# initialize weights randomly with mean 0. Must be same dimensions as x values e.g. np.random.random(Ninputs, Noutputs).
syn0 = 2*np.random.random((3,1)) - 1
 
for iter in range(20000):
 
    # forward propagation
    l0 = x                          # Base dataset
    l1 = sigmoid(np.dot(l0,syn0))    # Dot product of x values with weights to produce first layer of neural network

    # error between calculated value and true values.
    l1_error = y - l1
    
    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * sigmoid(l1,True)
    
    # update weights based on the errors calculated in the first iteration
    syn0 += np.dot(l0.T,l1_delta)
 
print("Output After Training:")
print(l1)

syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

for j in range(60000):

    # Feed forward through layers 0, 1, and 2
    l0 = x
    l1 = sigmoid(np.dot(l0,syn0))   #First layer of the neural network
    l2 = sigmoid(np.dot(l1,syn1))   #Final layer of the neural network

    # how much did we miss the target value?
    l2_error = y - l2

    if (j% 10000) == 0:
        print(f"Error:{np.mean(np.abs(l2_error))}")

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*sigmoid(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * sigmoid(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)  # Update the final layer weights
    syn0 += l0.T.dot(l1_delta)  # Update the first layer weights