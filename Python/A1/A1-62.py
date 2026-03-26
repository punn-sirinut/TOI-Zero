import math
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i==0:
            return False
    return True
x,y= map(int,input().split())
primes = []
for i in range(x,y+1):
    if is_prime(i):
        primes.append(i)
print(" ".join(map(str, primes)))
print(f"Total primes: {len(primes)}")