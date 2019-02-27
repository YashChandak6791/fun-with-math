#https://www.youtube.com/watch?v=aOT_bG-vWyg - My inspiration for this code

import itertools

length = 9
arrSquares = [None] * length
for i in range (1,length+1):
  arrSquares[i - 1] = i - 1

for itemComb in itertools.combinations(arrSquares, 9):
  for itemPerm in itertools.permutations(itemComb):
    row1 = itemPerm[0] + itemPerm[1] + itemPerm[2]
    row2 = itemPerm[3] + itemPerm[4] + itemPerm[5]
    row3 = itemPerm[6] + itemPerm[7] + itemPerm[8]

    col1 = itemPerm[0] + itemPerm[3] + itemPerm[6]
    col2 = itemPerm[1] + itemPerm[4] + itemPerm[7]
    col3 = itemPerm[2] + itemPerm[5] + itemPerm[8]

    diag1 = itemPerm[0] + itemPerm[4] + itemPerm[8]
    diag1 = itemPerm[2] + itemPerm[4] + itemPerm[6]

    bool rowEqual = False
    bool colEqual = False

    if (row1 = row2 = row3):
      print("Row: " + itemPerm)
      rowEqual = True
    if (col1 = col2 = col3):
      print("Col: " + itemPerm)
      colEqual = True

    if (colEqual && rowEqual):
      print("Row and Col: " + itemPerm)
      if (diag1 = diag2 = col1):
        print("Magic square: " + itemPerm)
