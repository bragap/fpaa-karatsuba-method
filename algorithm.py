
# Function to multiply two numbers using the Karatsuba algorithm
# x and y are the two numbers to be multiplied
# Returns the product of x and y
def karatsuba(x, y):
    # Base case: if x or y are small, do multiplication directly
    if x < 10 or y < 10:
        return x * y
    
    # Determine the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split the input numbers
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)
    
    # Calculate the three products recursively
    z0 = karatsuba(low_x, low_y)         # Inferior part
    z1 = karatsuba((low_x + high_x), (low_y + high_y)) # Middle part
    z2 = karatsuba(high_x, high_y)       # Superior part
    
    # Combine the results using the Karatsuba formula
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

