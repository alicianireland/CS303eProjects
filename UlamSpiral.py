# File: ulam_spiralpy
# Description: Display the Ulam Spiral of the matrix of the given dimension
# Assignment Number: 11
#
# Name: Alicia Ireland
# EID:  ani324
# Email: alicianireland@gmail.com
# Grader: Noah
#
# On my honor, Alicia Ireland, this programming assignment is my own work
# and I have not provided this code to any other student.


# Displays the Ulam Spiral and Integer Spiral of the matrix of the
# given dimension as input by the user. Through the program i is used
# to reference the row number and j is used to reference the column number.
def main():
    print("This program displays an Ulam Spiral of the specified size.")
    print()
    size = get_size()    
    width = int(size ** 2)
    
    # create the initial list of lists with all elements set to 0.
    spiral = [[0 for c in range(size)] for r in range(size)]
    
    num_matrix(spiral, size, width)
    integer_spiral(spiral, size)
    ulam_spiral(spiral, size)

    
# Asks the user for an odd integer greater than or equal to 1 and
# error check the response until they enter a positive odd value
def get_size():
    size = int(input(("Enter an odd integer greater than or equal to 1: ")))
    while (size % 2 == 0) or (size < 1):
        print(size, "is not an odd integer >= 1.")
        size = int(input(("Enter an odd integer greater than or"+
                          " equal to 1: ")))
    return size

        
# Create and display the Ulam Spiral where every integer that is a prime
# number is shown with an asterisk and non primes are spaces. Uses the
# spiral matrix previously created.
def ulam_spiral(spiral,size):
    print("----- The Ulam Spiral Size", size, "-----")
    for i in range(len(spiral)):
        row_tot =''
        for j in range(len(spiral[i])):
            cell = spiral[i][j]
            row_tot += "*" if isPrime(cell) else " "
        print(row_tot, sep = "")

        
# Create and return a matrix that is square based on the value entered
# by the user. The integer 1 is in the center of the matrix and the
# values increase by 1 spiraling out in a counter clockwise direction.
def num_matrix(matrix,width,num):
    # establishes what direction to add the numbers in the matrix
    delta_i = [0,-1,0,1] * num
    delta_j = [-1,0,1,0] * num
    
    i, j = (width - 1), (width - 1)
    #index of delta value that indicates to add index up/down/left/right
    k = 0
    while num >= 1:
        # Loop that adds the number in indicated direction, decreasing the
        # number inserted with every iteration. Continues as long as row and
        # column are in range of matrix and the current cell contains 0.
        while inbounds(i,j, matrix) and matrix[i][j] == 0:
            matrix[i][j] = num
            i += delta_i[k]
            j += delta_j[k]
            num -= 1        

        # When out of bounds, resest row & column to previous inbound index
        # and increments k so that the direction changes to spiral. Starts
        # first increment of new row/column based on new direction.
        i -= delta_i[k]
        j -= delta_j[k]
        k += 1
        i += delta_i[k]
        j += delta_j[k]
         
    return matrix


# Determine and return if the given row and column are
# within the range of the matrix. -1 is out of range.
def inbounds(i, j, matrix):
    return ((0 <= i < len(matrix))
            and (0 <= j < len(matrix[i])))


# Using the code from the book, determine if the number given
# from the matrix is prime or not and return True or False.
def isPrime(number):
    if number == 1:
        return False
    
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


# Print the Integer Spiral and separate every integer
# with a single space. There is no space following the last
# integer on a row or line.  
def integer_spiral(matrix, size):
    print("----- The Integer Spiral Size", size, "-----")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Print last number of every row w/out following space
            if j == size - 1:
                print(matrix[i][j])
            else:
                print(matrix[i][j],sep='',end = " ")
    print()


main()
