def fibo_gen():
    from math import factorial
    for x in range(1, 16):
        yield factorial(x)


for el in fibo_gen():
    print(el)
