import numpy as np
import utils
import argparse

def getTheta( file ):
    try :
        file1 = open( file, 'r' )
    except :
        print("Error: '" + file + "' not found")
        return []

    lines = file1.readlines()

    if len(lines) == 1 :
        data = data = lines[0].split( "," )
        data = [ float(data[0]), float(data[1]) ]
        file1.close()
        return np.array( data )
    else :
        file1.close()
        return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( "miles", help="number of miles", type=int )
    args = parser.parse_args()

    theta = getTheta( "theta.csv" )

    if len(theta) :
        print(utils.predict( theta, args.miles ))

if __name__ == "__main__":
    main()