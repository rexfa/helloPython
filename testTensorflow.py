
import tensorflow  as tfm
import numpy as npm
import matplotlib.pyplot as plt
#create data
x_data=npm.random.rand(100).astype(npm.float32)
y_data=x_data*0.1+0.3
###Create a structure
###start
Weights =tfm.Variable(tfm.random_uniform([1],-1.0,1.0))
biases = tfm.Variable(tfm.zeros([1]))
y=Weights*x_data + biases
#deviation and optimizer
loss= tfm.reduce_mean(tfm.square(y-y_data))
optimizer = tfm.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tfm.global_variables_initializer()
###end

#session
session = tfm.Session()
session.run(init) 

#train
#dispaly
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
t = npm.arctan2(x_data, y_data)

ax.scatter(x_data,y_data)
plt.ion()
plt.show()
for step in range(201):
    session.run(train)
    if step%20==0:
        xp = npm.linspace(0, 1, 3)
        yp = xp*session.run(Weights)+session.run(biases)
        ax.plot(xp,yp)
        #plt.ion()
        #plt.show()
        print(step,session.run(Weights),session.run(biases))
        plt.pause(1)

#show
#plt.show()
