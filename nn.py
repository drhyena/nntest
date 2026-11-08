import numpy as np
from sympy import diff
import random





class NeuralNetwork:
    def __init__(self,no_of_layers):
        self.layers = [] #input layer =0, output layer = n -1]
        self.no_of_layers = no_of_layers




    def create_layer(self,no_of_neurons,no_of_weight):
        weights = self.generate_random_weight(no_of_neurons,no_of_weight)
        layer = []
        for i in range(no_of_neurons):
            n = weights[:,i]
            layer.append(n)
        self.layers.append(layer)


    def generate_random_weight(self,no_of_neurons,no_of_weights):
        l = []
        for _ in range(no_of_neurons):
            for _ in range(no_of_weights):
                 l.append(np.random.randn())
                 print()

        l = np.array(l).reshape(no_of_weights,no_of_neurons)
        print(l.shape)
        return l                              # COLUMN INDICATES A NEURON. ALL OF A PARTICULAR NEURON'S WEIGHTS ARE UNDERNEATH IT'S COLUMN
                             # EVERY ROW CONTAINS THE LIST OF NEURONS ASSOSICATED WITH A PARTCULAR INPUT VALUE. 



 
    def sigmoid(self,x):
        return 1/(1+np.exp((-x)))


    def loss(self,out, Y):
        s =(np.square(out-Y))
        s = np.sum(s)/len(y)
        return(s)

    def feedforward(self): # sigmoid( wi.xi + a)
        output = self.layers[0]
        for x in self.layers[1:]:
            x = np.array(x)
            output = output.dot(x)
            output = self.sigmoid(output)
        return output 


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

network = NeuralNetwork(3)

network.layers.append(x[0])
network.create_layer(5,30)
network.create_layer(3,5)  

network.feedforward()

