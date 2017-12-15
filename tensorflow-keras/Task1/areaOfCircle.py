import tensorflow as tf
import numpy as np
import math

class AreaOfCircle:

    def __init__(self):
        self.sess = tf.Session()
        self.circumference, self.area, self.radius_var = self.buildGraph()

    def buildGraph(self):

        radius = tf.Variable(0.0, tf.float32)

        PI = tf.constant(math.pi)
        diameter = tf.multiply(tf.constant(2.0), radius )
        circumference = tf.multiply(diameter, PI)
        area = tf.multiply(PI, tf.pow(radius, tf.constant(2.0)))

        return (circumference, area, radius)

    def calculateAreaandRadius(self):
        while True:
            radius_str = input("Please provide the Radius: ")

            radius = float(radius_str)
            
            self.sess.run(tf.assign(self.radius_var, radius))
            circumference = self.sess.run(self.circumference)
            area = self.sess.run(self.area)
            print("Circumference : {}".format(circumference))
            print("Area : {}".format(area))

            choice = input("Do you want to calculate more (Y/n): ").strip().lower()
            if choice == 'n':
                break

        self.sess.close()
