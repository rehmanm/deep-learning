import tensorflow as tf

class AreaOfRectangle:

    def __init__(self):
        self.sess = tf.Session()
        self.length, self.width, self.area = self.buildGraph()

    def buildGraph(self):
        length = tf.Variable(0.0, tf.float32)
        width = tf.Variable(0.0, tf.float32)
        area = tf.multiply(length, width)

        return (length, width, area)

    def calculateAreaandRadius(self):

        while True:

            length = float(input("Please provide Length: "))
            width = float(input("Please provide Width: "))

            self.sess.run(tf.assign(self.length, length))
            self.sess.run(tf.assign(self.width, width))
            area = self.sess.run(self.area)
            print("Area: {}".format(area))

            choice = input("Do you want to calculate more (Y/n): ").strip().lower()
            if choice == 'n':
                break

        self.sess.close()