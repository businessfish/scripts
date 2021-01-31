### author:     noah michaels
### 
###
### miller-rabin primality test

import sys
import random

#num = 0
sec = 1    # test sec param

# main primality test
# test <sec> times
# the security parameter determines probability of primality
# returns the probability of primality of x
def primetest(x):
    # initialize total tries and successes
    tries = 0
    primes = 0

    # get number of times temp is half-able
    halves = 0
    temp = x - 1
    while temp % 2 == 0:
        temp = temp // 2
        halves += 1
    
    # test for composite num <sec> times
    for tests in range(sec):
        tries += 1
        rand = random.randrange(2, x - 2)
        power = pow(rand, temp, x)
        if power != 1:
            i = 0
            while power != (x - 1):
                tries += 1
                if i == halves - 1:
                    break
                else:
                    i += 1
                    power = (power ** 2) % x
                primes += 1
        else:
            primes += 1
                
    prob =100 * ( primes * 1.0) / tries
    return round(prob, 3)


# arbitrary tests for edge cases and small numbers
# returns the probability of num being prime
def isPrime(num):
    if num < 2:
        return 0
    #elif num == 3:
    #    return 100
    #elif num % 2 == 0 or num % 3 == 0:
     #   return 0
    
    # run the main test
    #print('running primetest...', str(num))
    return  primetest(num)


# test 10 large odd ints
num = 0
for i in range(100):
    # get an odd number to test
    while num == 0 or num % 2 == 0:
        num = random.randrange(105000, 115000)
        
    # test the number
    print (isPrime(num), '\t% prime probability for', str(num))
    num = 0
