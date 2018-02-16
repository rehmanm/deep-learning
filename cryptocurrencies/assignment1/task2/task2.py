import pandas as pd 
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"

def load_data():
    

    data = pd.read_csv('data.csv')
    data = data[(data.timestamp >= '2018-01-01' ) & (data.timestamp <='2018-01-31')]


    index = pd.read_csv('index.csv')
    index = index[(index.Date >= '2018-01-01' ) & (index.Date <= '2018-01-31')]

    #Calculate Return
    x_train = (index.Close - index.Open)*100.0/index.Open

    y_train = (data.close - data.open)*100.0/data.open

    
    return x_train, y_train




def model(X, w):
    return tf.add(tf.multiply(X, w[1]), w[0])


def tf_regression_model(x_train, y_train):
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)
    W = tf.Variable([0.0, 0.0], name='parameters')
    learning_rate = 0.001
    w_val = [1.0, 1.0]
    learning_epoch = 1000

    y_model = model(X, W)
    
    cost = tf.square(Y-y_model)
    train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)

    for epoch in range(learning_epoch):
        for x, y in zip(x_train, y_train):
            sess.run(train_op, feed_dict = {X:x, Y:y})
            print(sess.run(cost, feed_dict = {X:x, Y:y}))
    
    w_val = sess.run(W)

    sess.close()
    return w_val


print('start program')
x_train, y_train = load_data()

print('applying tensorflow')
w_val = tf_regression_model(x_train, y_train)
y_learned = np.multiply(x_train, w_val[1]) + w_val[0]
print(w_val)
plt.scatter(x_train, y_train, color='g')
plt.plot(x_train, y_learned, color='r')
plt.show()