import math
def PrimeCheck(a):
  for j in range(2,math.floor(math.sqrt(a)),2):
    if a%j == 0:
      return False
  return True
num = 2
count = 0
while(True):
  if (PrimeCheck(num)):
    count += 1
    print('Prime: ' + str(num) + '. Count: ' + str(count))
  num += 1
