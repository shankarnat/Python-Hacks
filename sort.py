#function overloading
fruits = ['banana', 'apple' , 'pear', 'grape']


#this reverses the word
def reversed(val):
    return val[::-1]


# Simple sort function is being called here
print(sorted(fruits))
# Sort based on the length of the words
print(sorted(fruits, key = len))
#Sort based on the reversed word , here we are using function overloading
print(sorted(fruits, key = reversed))
