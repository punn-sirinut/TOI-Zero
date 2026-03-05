from math import isqrt
x = int(input())
l = isqrt(x)
if l * l < x:
    l += 1
print(2 * (l - 1) - (x % 2 != l % 2))