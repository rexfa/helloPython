import tensorflow as tfm
import numpy as npm
import matplotlib.pyplot as plt
#增加层函数，输入值，输入值大小，输出值大小，激励函数
def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tfm.Variable(tfm.random_normal([in_size,out_size]))
    biases = tfm.Variable(tfm.zeros([1,out_size]) + 0.1)
    Wx_plus_b = tfm.matmul(inputs,Weights)+ biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

#make target data with some noise
x_data = npm.linspace(-1,1,300)[:,npm.newaxis]
noise = npm.random.normal(0,0.05,x_data.shape)
y_data = npm.square(x_data)+0.5+noise

#Show data
##plt.scatter(x_data,y_data)
##plt.show()

# Define placeholder for inputs to the network
xs = tfm.placeholder(tfm.float32,[None,1])
ys = tfm.placeholder(tfm.float32,[None,1])
# Add a hide layer
l1 = add_layer(xs,1,10,tfm.nn.relu)
# Add an output layer
prediction = add_layer(l1,10,1,None)

# The lose between prediction and real data
loss = tfm.reduce_mean(tfm.reduce_sum(tfm.square(ys-prediction),reduction_indices=[1]))
train_step = tfm.train.GradientDescentOptimizer(0.1).minimize(loss)

# Session
session = tfm.Session()
inti = tfm.initialize_all_variables()
session.run(inti)

# draw the real data
fig1 = plt.figure()
ax =fig1.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.ion()
plt.show()


# train 2000 times
for i in range(2000):
    session.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = session.run(prediction,feed_dict={xs:x_data})

        # show the prediction
        lines= ax.plot(x_data,prediction_value,'r-',lw=5)
        plt.pause(1)

