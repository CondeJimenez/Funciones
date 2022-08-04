def factorial(num):
    tmp = 1
    for i in range(num):
        i = i + 1
        tmp *= i
    return tmp
print(factorial(5))