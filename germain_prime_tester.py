def is_prime(numCalc):
  for j in range(2,numCalc-1):
    if numCalc%j==0:
      return False
  return True

count = 0
for i in range(0,50000):
  if is_prime(i):
    if is_prime(2*i+1):
      print(str(i) + ': Yes')
      count += 1
print('Count: ' + str(count))
