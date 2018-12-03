# def mul_fun(n):
#  return lambda a : a*n

# a_fun = mul_fun(10)
# b_fun = mul_fun(4)

# print a_fun(10)
# print b_fun(4)


def sum_fun(n):
    return lambda a: a*n


x = sum_fun(10)

print(x(4))
