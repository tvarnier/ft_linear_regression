def predict( theta, mileage ):
    return  theta[0] + theta[1] * mileage

def cost_function( mileage, price , theta ):
    nbrData = len( mileage )
    error = 0.0
    for i in range( nbrData ):
        error += predict( theta, mileage[i] ) - price[i]
    return abs( error / nbrData )

def priceFromNormalizeMileage( mileage, price, theta ):
    minPrice = float(min(price))
    maxPrice = float(max(price))
    return float(predict( theta, mileage ) * (maxPrice - minPrice) + minPrice)

def minAndMaxPrice( price, theta ):
    return priceFromNormalizeMileage( 0.0, price, theta ), priceFromNormalizeMileage( 1.0, price, theta )

def realTheta( mileage, price, theta ):
    (minPrice, maxPrice) = minAndMaxPrice( price, theta )
    minMileage = float(min( mileage ))
    maxMileage = float(max( mileage ))
    tmp1 = ( maxPrice - minPrice ) / ( maxMileage - minMileage )
    tmp0 = minPrice - ( tmp1 * minMileage )
    return ( tmp0, tmp1 )