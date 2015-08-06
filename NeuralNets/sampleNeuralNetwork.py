import os
import random
from neuralnetwork import *



inputs = [[0,0],[0,1],[1,0],[1,1]]
targets = [[0],[1],[1],[0]]



random.seed(0) # to get repeatable results
input_size = 2 # each input is a vector of length 2
num_hidden = 2 # we'll have 2 neurons in hidden layer
output_size = 1 #we need 10 outputs for each input


# each hidden neuron has one weight per input, plus a bias weight
hidden_layer = [[random.random() for __ in range(input_size + 1)] for __ in range(num_hidden)]

# each output neuron has one weight per hidden neuron, plus a bias weight
output_layer = [[random.random() for __ in range(num_hidden +1)] for __ in range(output_size)]

# the network starts out with random_weights
network = [hidden_layer,output_layer]


for __ in range(100000):
    for input_vector,target_vector in zip(inputs,targets):
           backpropagate(network,input_vector,target_vector)


test_input = [1,0]

# show output for input {1,0}
print 'input {} outputs {}'.format(test_input,feed_forward(network,test_input)[-1])