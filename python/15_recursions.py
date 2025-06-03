"""Recursion of printing first N natural numbers"""
def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=" ")

"""Reverse Recursion of printing first N natural numbers"""
def printNReverse(n):
    if n>0:
        print(n,end=" ")
        printNReverse(n-1)

"""Recursion of printing first N odd numbers"""
def printNOdd(n):
    if n>0:
        printNOdd(n-1)
        print((2*n)-1,end=" ")

"""Recursion of printing first N even numbers"""
def printNEven(n):
    if n>0:
        printNEven(n-1)
        print(n*2,end=" ")

"""Reverse recursion of printing first N odd numbers"""
def printNOddReverse(n):
    if n>0:
        print((2*n)-1,end=" ")
        printNOddReverse(n-1)

"""Reverse recursion of printing first N Even numbers"""
def printNEvenReverse(n):
    if n>0:
        print(2*n,end=" ")
        printNEvenReverse(n-1)

"""Recursion for Sum of N natural numbers"""
def sumOfN(n):
    if n>0:
        return n+sumOfN(n-1)
    return 0 

"""Recursion for sum of first N Odd numbers"""
def sumOfNOdd(n):
    if n>0:
        return (2*n-1)+sumOfNOdd(n-1)
    return 0

"""Recursion for sum of first N Even numbers"""
def sumOfNEven(n):
    if n>0:
        return (2*n)+sumOfNEven(n-1)
    return 0

"""Recursion for sum of Factorial of a number"""
def sumOfFactorial(n):
    if n>0:
        return n*sumOfFactorial(n-1)
    return 1

"""Recusion for sum of first N square numbers"""
def sumOfNSquare(n):
    if n>0:
        return (n*n) + sumOfNSquare(n-1)
    return 0






"""Driver Code"""

# printN(10)
# print("\n")
# printNReverse(10)
# print("\n")
# printNOdd(10)
# print("\n")
# printNEven(10)
# print("\n")
# printNOddReverse(10)
# print("\n")
# printNEvenReverse(10)
# print("\n")
# print(sumOfN(5))
# print("\n")
# print(sumOfNOdd(3))
# print("\n")
# print(sumOfNEven(1))
# print("\n")
# print(sumOfFactorial(5))
# print("\n")
# print(sumOfNSquare(4))