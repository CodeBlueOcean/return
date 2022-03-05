# another example
def sum(num1, num2):
    return num1 + num2

print(sum(10,5))

[1,2,3].clear()

# another example
# def sum(num1, num2):
#     print('hiii')
#     num1 + num2

# Should do one thing really well.  
# Should return something 

print(sum(10,5))

[1,2,3].clear()

# another example

# total = sum(10,5)
# print(sum(10,total))

# another example shorthand

print(sum(10,sum(10,5)))

# another example

def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func

total = sum(10, 20)
print(total) 

# another example

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total = sum(10, 20)
print(total) 


# another example

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)
    return 5
    print('hello')

total = sum(10, 20)
print(total) 

