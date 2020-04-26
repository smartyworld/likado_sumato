#!/usr/bin/python3
import math
upto=200
primes = set(range(upto))
primes.remove(0)
primes.remove(1)
primes.add(upto)
for i in range(upto,1,-1):
    for j in range(math.floor(math.sqrt(i)),1,-1):
        if i%j==0:
            primes.discard(i)
print(primes)

