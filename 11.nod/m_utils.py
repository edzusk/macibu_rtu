from math import prod

def sum_prod(*seq):
    sum_l= []
    for n in seq:
        sum_l.append(prod(n))
    return sum(sum_l)