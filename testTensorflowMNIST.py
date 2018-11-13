import tensorflow as tf
import numpy as np

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
def compute_accuracy(v_xs,v_ys):
    global prediction
    y_pre = session.run(prediction,feed_dict={xs:v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = session.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result


from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

xs = tf.placeholder(tf.float32,[None,784]) #28*28
ys = tf.placeholder(tf.float32,[None,10])
prediction = add_layer(mnist,784,10,1,activation_function=tf.nn.softmax)

cross_entropy= tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1])) #loss

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
session = tf.Session()
session.run(tf.global_variables_initializer())


for i in range(1000):
    batch_xs,batch_xy = mnist.train.next_batch(100)
    session.run(train_step,feed_dict={xs:batch_xs,ys:batch_xy})
    if i%50==0:
        print(compute_accuracy(mnist.test.images,mnist.test.labels))
