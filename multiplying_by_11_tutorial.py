def carry(fnum, mnum, lnum):
  print('\nSince ' + str(mnum) + ' is more than one digit, we only write one digit of the sum, namely, the one\'s digit.')
  print('\n** ' + str(int(mnum%10)) + str(lnum) + ' **')
  stall()
  print('\nThen we remember the carry of ' + str(int((mnum-mnum%10)/10)) + '.')
  stall()
  print('\nThe next step is to simply write the ten\'s digit of the original number. However, before we write it, we must add the carry.')
  stall()
  print('\n' + str(fnum) + ' + ' + str(int((mnum-mnum%10)/10)) + ' = ' + str(int((mnum-mnum%10)/10) + fnum))
  print('\n** ' + str(int((mnum-mnum%10)/10) + fnum) + str(int(mnum%10)) + str(lnum) + ' **')
  stall()


def teach112(num):
  print('\nFirst, write the one\'s digit of the answer.')
  print('\n** ' + str(num%10) + ' **')
  lastnum = int(num%10)
  firstnum = int((num-num%10)/10)
  midnum = firstnum+lastnum
  stall()
  print('\nNext, add the one\'s and the ten\'s digit.')
  print('\n' + str(firstnum) + ' + ' + str(lastnum) + ' = ' + str(midnum))
  if midnum>9:
    carry(firstnum, midnum, lastnum)
  else:
    print('\nWrite this as the ten\'s digit of your answer.')
    print('\n** ' + str(midnum) + str(lastnum) + ' **')
    stall()
    print('\nThe next step is to simply write the ten\'s digit of the original number.')
    print('\n** ' + str(firstnum) + str(midnum) + str(lastnum) + ' **')
    stall()

def multiply11():
  print('\nThe trick is best explained with some examples. \n\nLet us multiply 24 by 11.')
  teach112(24)
  print('Now, let\'s try a tougher example. 57 times 11:')
  teach112(57)
  print('Now, time for some practice:')
  practice()

def stall():
  while (input('Send \'c\' to continue')!='c'):
    print('Please try again.')

def practice():
  listL = [12,34,37,85,93,29]
  for i in listL:
    answer = input('What is ' + str(i) + '*11?')
    while(int(answer)!=i*11):
      print('Please try again.')
      answer = input('What is ' + str(i) + '*11?')
    print('Correct!')
    print('Next problem :)')
  numabc = input('OK. Your turn. Choose a two-digit number to multiply by 11.')
  for j in listL:
    if int(numabc)==j:
      print('Please choose another number.')
      numabc = input('OK. Your turn. Choose a two-digit number to multiply by 11.')
  listL.append(int(numabc))
  answerA = input('What is ' + str(listL[6]) + '*11?')
  while(int(answerA)!=listL[6]*11):
    print('Please try again.')
    answerA = input('What is ' + str(listL[6]) + '*11?')
  print('Correct!')

print('Yash Chandak\nMultiplying by 11\n\n')
name = input('Hello! What is your name: ')
print ('Hello ' + name + '! Today we will learn how to multiply by 11. ')
multiply11()
print('Thank you for learning!')
