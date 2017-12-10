#Exercise to try out options on map, filter functions in Python.

#function that would be used for map and filter methods
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

fact = factorial

#Prints the factorial of numbers from 0 to 4; range(5) generates from 0-4
print(list(map(fact, range(5))))

#Print Factorial only for Odd Numbers
print(list(map(fact, filter(lambda x: x%2, range(5)))))

#Print Factorial only for Even Numbers
print(list(map(fact, filter(lambda x: x%2-1, range(5)))))
