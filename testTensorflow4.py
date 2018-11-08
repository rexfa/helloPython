import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#增加层函数，输入值，输入值大小，输出值大小，激励函数
def add_layer(inputs,in_size,out_size,n_layer,activation_function=None):
    layer_name = 'layer%s'%n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size]))
            tf.summary.histogram(layer_name + '/weight',Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
            tf.summary.histogram(layer_name + '/biases',biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs,Weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name+'/outputs',outputs)
        return outputs

#make target data with some noise
x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)+0.5+noise

#Show data
##plt.scatter(x_data,y_data)
##plt.show()

# Define placeholder for inputs to the network
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1],name='x_in')
    ys = tf.placeholder(tf.float32,[None,1],name='y_in')
# Add a hide layer
l1 = add_layer(xs,1,10,n_layer=1,activation_function=tf.nn.relu)
# Add an output layer
prediction = add_layer(l1,10,1,n_layer=2,activation_function=None)

# The lose between prediction and real data
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
    tf.summary.scalar('loss',loss)
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


# Session
session = tf.Session()

# merge all summary
merged = tf.summary.merge_all()
# writer logs
writer = tf.summary.FileWriter("logs/",session.graph)

# inti = tf.initialize_all_variables()   will discard
inti = tf.global_variables_initializer()
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
        prediction_value = session.run(merged,feed_dict={xs:x_data, ys: y_data})
        writer.add_summary(prediction_value, i)
        
        # show the prediction
        prediction_value_list = session.run(prediction,feed_dict={xs:x_data})
        lines= ax.plot(x_data,prediction_value_list,'r-',lw=5)

        plt.pause(1)

        
#terminal command 搭建图纸
#tensorboard --logdir logs