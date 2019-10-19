###################
# HUGHES, JOSHU L
# CS325 OSU
# MERGE SORT
# ASSIGNMENT 1
# 07 OCT 2019
##################


import fileHandler


# type of sorting method, also output file name
SORT_TYPE = "merge"


# path to input file
filePath = "data.txt"
# path to output file
savePath = "{}.txt".format(SORT_TYPE)





def mergeSort(lst, p, r):
  '''REF PSUDO CODE FROM TEXT (INTO TO ALGORTHIMS V3)'''
  #if p < r
  #  q = |(p + r) / 2|
  #  MergeSort(A, p, q)
  #  MergeSort(A, q + 1, r)
  #  Merge(A, p, q, r)

  if p < r:
    q = (p + r) / 2

    mergeSort(lst, p, q)
    mergeSort(lst, q + 1, r)
    merge(lst, p, q, r)




def merge(lst, p, q, r):
 
  '''REF PSUDO CODE FROM TEXT (INTO TO ALGORTHIMS V3)'''
  #n_1 = q - p + 1
  #n_2 = r - q
  #let L[1..n_1] and R[1..n_2 + 1] be new arrays
  #for i = 1 to n_1
  #  L[i] = A[p + i - 1]
  #for j = 1 to n_2
  #  R[j] = A[q + j]
  #L[n_1 + 1] = sentinel
  #R[n_2 + 1] = sentinel
  #i = 1
  #j = 1
  #for k = p to r
  #  if L[i] <= R[j]
  #    A[k] = L[i]
  #    i = i + 1
  #  else a[k] = R[j]
  #    j = j + 1

  n_1 = q - p + 1
  n_2 = r - q

  llst = lst[:n_1]
  rlst = lst[len(lst) - n_2:]

  for i in range(0, n_1):
    llst[i] = lst[p + i]

  for j in range(0, n_2):
    rlst[j] = lst[q + 1 + j]


  i = 0
  j = 0
  ##########################################################
  #for k = p to r
  #  if L[i] <= R[j]
  #    A[k] = L[i]
  #    i = i + 1
  #  else a[k] = R[j]
  #    j = j + 1

  k = p

  x = 0 

  '''REF://www.geeksforgeeks.org/merge-sort/'''
  
  while i < n_1 and j < n_2:
    # x = i + j
    # print (n_1, n_2, r)

    x += 1
    if int(llst[i]) <= int(rlst[j]):
      lst[k] = llst[i]
      i += 1

    else:
      lst[k] = rlst[j]
      j += 1

    k += 1

  while i < n_1:
    lst[k] = llst[i]
    i += 1
    k += 1

  while j < n_2:
    lst[k] = rlst[j]
    j += 1
    k += 1

  ##############################

def main():
  # get contents of input file
  fileContent = fileHandler.parseFile(filePath)

  for lst in fileContent[0:100]:
    mergeSort(lst, 0, len(lst) - 1)

 

  # write sorted data to output file
  fileHandler.writeFile(savePath, fileContent)



if __name__ == "__main__":
  print("{}{} Sort".format(SORT_TYPE[0].upper(), SORT_TYPE[1:]))
  main()

