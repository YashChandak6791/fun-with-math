#https://en.wikipedia.org/wiki/Mersenne_prime - Use for comparison to Mercenne Primes
#https://www.youtube.com/watch?v=lEvXcTYqtKU - My inspiration for this code
#https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test - Logic for LLT
#Since LLT only works for p>2, I originally print the case for p=2
#(and assume it falls in the range)
#Compare to OEIS list A000043: https://oeis.org/A000043

import math

def is_prime(numCalc):
  for j in range(2,math.floor(math.sqrt(numCalc)),2):
    if numCalc%j==0:
      return False
  return True

print('2^2-1: Yes')
for powerNum in range(1,5000):
  if (is_prime(powerNum)):
    power = 2**powerNum-1
    num = 4
    for i in range(1,powerNum):
      if power>num:
        num = num**2-2
      elif i<(powerNum-1):
        num = (num % power)**2-2
      else:
        num = num % power
    if num==0:
      print('2^' + str(powerNum) + '-1')
