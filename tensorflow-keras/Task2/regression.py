import numpy as np
from printGraph import getData
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import tensorflow as tf


def model(X, w):
    return tf.multiply(X, w)


def applyRegression(x_train, y_train):
    learning_rate = 0.01
    training_epochs = 100
    #x_train, y_train = getData()
    m = x_train.size
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)
    w = tf.Variable(0.0, name="weights")
    y_model = model(X, w)
    cost = tf.square(Y - y_model)

    train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    for epoch in range(training_epochs):
        i = 0
        for (x, y) in zip(x_train, y_train):
            # if i == 50:
            #     print(epoch, x, y, sess.run(w))
            #     print(sess.run(cost, {X:x, Y:y}))
            # i = i + 1
            sess.run(train_op, {X:x, Y:y})

    w_val = sess.run(w)
    print("w_val:" + str(w_val))
    sess.close()

    #print(set(zip(x_train, y_train)))
    fig= plt.figure(2)
    fig.clear()
    plt.title("Linear Regression with one variable with parameter: "  +  str(w_val))
    plt.scatter(x_train, y_train, color="r", marker='x')
    y_learned = x_train * w_val
    #comparison = np.hstack((y_train.reshape(m, 1), y_learned.reshape(m, 1)))
    #print("Comparison: {}".format(comparison))
    plt.plot(x_train, y_learned, 'b')
    plt.draw()




