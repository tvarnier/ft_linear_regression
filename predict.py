import numpy as np
import utils
import argparse

def error( file ):
    file.close()
    print("Error: Incorrect `theta.csv` content")
    return []

def getTheta( file ):
    try :
        file1 = open( file, 'r' )
    except :
        print("Error: '" + file + "' not found")
        return []

    lines = file1.readlines()

    if len(lines) == 1 :
        data = lines[0].split( "," )
        if len(data) == 2:
            try :
                data = [ float(data[0]), float(data[1]) ]
            except ValueError :
                return error( file1 )
            file1.close()
            return np.array( data )
        return error( file1 )
    else :
        return error( file1 )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( "miles", help="number of miles", type=int )
    args = parser.parse_args()

    theta = getTheta( "theta.csv" )

    if len(theta) :
        print(utils.predict( theta, args.miles ))

if __name__ == "__main__":
    main()
