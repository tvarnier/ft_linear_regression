import numpy as np
import matplotlib.pyplot as plt
import utils
import argparse
from graph import Graph

def learn( mileage, price , options, g):
    learningRate = options['learningRate']
    nbrIterations = options['nbrIterations']

    theta = [ 0.0, 0.0]

    for i in range( nbrIterations ):
        error0 = lambda m, p: utils.predict( theta, m ) - p
        error1 = lambda m, p: (utils.predict( theta, m ) - p) * m

        sum0 = sum( error0( mileage, price ) )
        sum1 = sum( error1( mileage, price ) )

        if options['visualizer'] : g.update(mileage, price, theta)

        theta[0] -= ( sum0 / len( mileage ) ) * learningRate
        theta[1] -= ( sum1 / len( mileage ) ) * learningRate

    if options['visualizer'] : g.update(mileage, price, theta)
    if options['visualizer'] : g.show()
    
    return theta

def normalize( data ):
    tmp = data.copy()
    minArray = min( tmp )
    maxArray = max( tmp )
    f = lambda x: ( x - minArray ) / ( maxArray - minArray )
    norm = np.vectorize( f )
    tmp = norm(tmp)
    return tmp

def getData( file ):
    data = []
    file1 = open( file, 'r' ) 
    lines = file1.readlines()
    
    count = -1
    for line in lines:
        count += 1
        if count == 0:
            continue
        t = line.split( "," )
        t = [ float(t[0]), float(t[1]) ]
        data.append( t )

    file1.close()

    return np.array( data )

def setTheta( file, data ):
    f = open(file, "w")
    f.write(','.join(map(str,data)))
    f.close

def main():
    options = {
        'nbrIterations': 100,
        'learningRate': 0.5,
        'visualizer': False
    }

    parser = argparse.ArgumentParser()
    parser.add_argument( "data", help="Data's file", type=str )
    parser.add_argument( "-i", "--iterations", nargs='?', dest="iterations", help="Number of Iterations", type=int, const=options['nbrIterations'], default=options['nbrIterations'])
    parser.add_argument( "-lr", "--learningRate", nargs='?', dest="learningRate", help="Learning Rate", type=float, const=options['learningRate'], default=options['learningRate'])
    parser.add_argument("-v", "--visualizer", help="Display Visualizer", action="store_true")
    args = parser.parse_args()

    options['nbrIterations'] = args.iterations
    options['learningRate'] = args.learningRate
    options['visualizer'] = args.visualizer

    data = getData( args.data )
    data = data[data[:, 0].argsort()]

    mileage = np.array( data[ :, 0 ] )
    price = np.array( data[ :, 1 ] )

    mileageNormalize = normalize( mileage )
    priceNormalize = normalize( price )

    g = None
    if options['visualizer'] : g = Graph(mileage, price, options['nbrIterations'])

    theta = learn( mileageNormalize, priceNormalize, options, g)

    setTheta( "theta.csv", utils.realTheta( mileage, price, theta ) )

    print(theta)
    print(utils.realTheta( mileage, price, theta ))
 
if __name__ == "__main__":
    main()