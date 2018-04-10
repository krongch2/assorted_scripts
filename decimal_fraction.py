import numpy as np

def factors(n):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l

def fraction(n):
    n_str = str(n)
    decimal_part = n_str[n_str.find('.') + 1:]
    numer = int(n * 10**len(decimal_part))
    denom = int(10**len(decimal_part))
    for factor in factors(numer):
        if factor in factors(denom):
            gcf = factor
    return (numer / gcf, denom / gcf)

print(fraction(0.75))
