import math

def isPrime(num):
  a = 2
  while (a<=math.floor(math.sqrt(num))):
    if num%a==0 and num > a:
      return False
    a += 1
  return True

def primes():
  maxNum = int(input('Until what number do you want to see the primes: '))
  isPrimeVar = True
  if maxNum <=1:
    print ('No primes below ' + str(maxNum))
  else:
    i = 2
    while (i<=maxNum):
      a = 2
      isPrimeVar = True
      while (a<=math.floor(math.sqrt(i))):
        if i%a==0 and i > a:
          isPrimeVar = False
        a += 1
      if isPrimeVar:
        print(i)
      i += 1

def factors(num):
  a = 1
  listFactors = []
  while (a<=num):
    if num%a==0:
      listFactors.append(a)
    a += 1
  return listFactors

def AbunDefPerf():
  testNum = int(input('What number do you want to check if Abundant, Deficient, or Perfect: '))
  listL = factors(testNum)
  sumList = 0
  for i in listL:
    sumList += i
  if (sumList == 2*testNum):
    print(str(testNum) + ' is Perfect!')
  elif (sumList > 2*testNum):
    print(str(testNum) + ' is Abundant!')
  else:
    print(str(testNum) + ' is Deficient!')

def printFactors():
  testVal = int(input('What number do you want to see the factors of: '))
  listVal = factors(testVal)
  for i in listVal:
    print(i)


primes()
AbunDefPerf()
printFactors()
