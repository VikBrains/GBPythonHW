def res_abs(x):
    return x if x >= 0 else x * -1


def my_pow(x, y):
    res = x
    for i in range(res_abs(y) - 1):
        res *= x
    if y < 0:
        res = 1 / res
    return res


try:
    basis = int(input("x = "))
    degree = int(input("y = "))
    print(f"x ** y =  {my_pow(basis, degree)}")
except ValueError as e:
    print(e)


my_func = lambda base, degree: base ** degree
base = int(input("x = "))
degree = int(input("y = "))
print(my_func(base, degree))