import numpy as np
import matplotlib.pyplot as plt
import os
import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"


X = np.linspace(-1, 1, 101)
#Y = np.power(X, 2) + np.random.randn(X.size) * 0.03
Y = 2 * X + np.random.randn(X.size) * 0.33
learning_rate = 0.01
training_epoch = 75

def model(X1, w):
    return tf.multiply(X1, w)


x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

w = tf.Variable(0.0, name="weights")
y_model = model(x, w)

cost = tf.square(y - y_model)

train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

sess = tf.Session()
init = tf.global_variables_initializer()

sess.run(init)

for epoch in range(training_epoch):
    for (x1, y1) in zip(X, Y):
        sess.run(train_op, feed_dict={x: x1, y: y1})
        w_val = sess.run(w)
        print(x1, y1, w_val)

w_val = sess.run(w)

sess.close()

y_learned = np.power(X, 1) * w_val


plt.scatter(X, Y, marker='x', color='r')
plt.plot(X, y_learned, color='b')
plt.title("weight = " + str(w_val))
plt.show()

print('done')