import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Inputs
x1 = 0.5
x2 = 0.8

# Weights from input to hidden layer
w1 = 0.2
w2 = 0.4
w3 = 0.7
w4 = 0.9

# Weights from hidden to output layer
w5 = 0.3
w6 = 0.5

# Biases
b1 = 0.1
b2 = 0.2
b3 = 0.3

# Hidden layer
h1 = sigmoid(x1 * w1 + x2 * w2 + b1)
h2 = sigmoid(x1 * w3 + x2 * w4 + b2)

# Output layer
output = sigmoid(h1 * w5 + h2 * w6 + b3)

print("Hidden Neuron 1:", h1)
print("Hidden Neuron 2:", h2)
print("Final Output:", output)
