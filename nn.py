import numpy as np
from sympy import diff
import random

# A
a =[0, 0, 1, 1, 0, 0,
   0, 1, 0, 0, 1, 0,
   1, 1, 1, 1, 1, 1,
   1, 0, 0, 0, 0, 1,
   1, 0, 0, 0, 0, 1]
# B
b =[0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 1, 0,
   0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 1, 0,
   0, 1, 1, 1, 1, 0]
# C
c =[0, 1, 1, 1, 1, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 0, 0, 0, 0,
   0, 1, 1, 1, 1, 0]

# Creating labels
y =[[1, 0, 0],
   [0, 1, 0],
   [0, 0, 1]]

x = (np.array(a).reshape(1,30),np.array(b).reshape(1,30),np.array(c).reshape(1,30))
#newarr = arr.reshape(4)

print(x[0])


class Neuron:
    def __init__(self,weight):
        self.weight = weight 





class NeuralNetwork:
    def __innit__(self,no_of_layers):
        self.layers = []
        self.no_of_layers = no_of_layers



    def create_layer(self,no_of_neurons,weights):
        
        for i in range(no_of_neurons):
            n = Neuron(weights[i])

            self.layers.append(n)


    def generate_random_weight(self):
        n = random.randint()

        pass

    def sigmoid()