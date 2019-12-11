import math

def is_prime(numCalc):
  for j in range(2,math.floor(math.sqrt(numCalc)),2):
    if numCalc%j==0:
      return False
  return True

def primes():
  maxNum = int(input('Until what number do you want to see the primes: '))
  isPrimeVar = True
  if maxNum <=1:
    print ('No primes below ' + str(maxNum))
  else:
    i = 2
    while (i<=maxNum):
      if(is_prime(i)):
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
  sumList = sum(listL)
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
