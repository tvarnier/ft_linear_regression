import numpy as np
import matplotlib.pyplot as plt
import utils

import time



class Graph:
    def __init__(self, mileage, price, nbrIterations):
        self.nbrIterations = nbrIterations
        self.mileage = mileage
        self.price = price
        self.lastUpdate = 0
        self.updateFrequency = nbrIterations / 2

        self.fig  = plt.figure(figsize=(10, 7))

        self.thetaAxis= plt.subplot(2, 1, 1)

        self.accuracyAxis = plt.subplot(2, 2, 3)

        self.costAxis = plt.subplot(2, 2, 4)

        self.cost_history = []
        self.precision_history = []

    def update(self, mileage, price, theta):
        precision = 1 - abs( utils.cost_function( mileage, price, theta ) ** 2)
        self.precision_history.append( precision )

        cost = utils.cost_function( mileage, price, theta )
        self.cost_history.append( cost )

        milliseconds = int(round(time.time() * 1000))

        if (milliseconds - self.lastUpdate) > self.updateFrequency :
            self.lastUpdate = milliseconds
            
            self.thetaAxis.cla()
            self.thetaAxis.set_title("Theta")
            self.thetaAxis.plot( self.mileage, self.price, 'ro' )
            self.thetaAxis.plot( [ self.mileage[0], self.mileage[len(self.mileage) - 1] ], utils.minAndMaxPrice( self.price, theta ) )
            
            self.accuracyAxis.plot( range(len(self.precision_history)), self.precision_history, 'b' )
            self.accuracyAxis.set_title("Accuracy")
            self.accuracyAxis.set_ylim( [ 0, 1.01 ])
            self.accuracyAxis.set_xlim( [ - self.nbrIterations * 0.05, self.nbrIterations * 1.05 ])

            self.costAxis.plot( range(len(self.cost_history)), self.cost_history, 'r')
            self.costAxis.set_title("Cost")
            self.costAxis.set_ylim( [ -0.1, 1.01 ])
            self.costAxis.set_xlim( [ - self.nbrIterations * 0.05, self.nbrIterations * 1.05 ])
        plt.pause(0.000000001)

    def show(self):
        plt.show()

