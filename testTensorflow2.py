import tensorflow as tfm
import numpy as npm
import matplotlib.pyplot as plt

def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tfm.Variable(tfm.random_normal([in_size,out_size]))
    biases = tfm.Variable(tfm.zeros([1,out_size]) + 0.1)
    Wx_plus_b = tfm.matmul(inputs,Weights)+ biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs