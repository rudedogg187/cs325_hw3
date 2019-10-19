# CS325 OSU
# INSERT SORT
# ASSIGNMENT 2
# 10 OCT 2019
##################
#ref: 	https://en.wikipedia.org/wiki/Stooge_sort
#ref:	https://www.geeksforgeeks.org/stooge-sort/



import fileHandler
import cleanup


# type of sorting method, also output file name
SORT_TYPE = "stooge"


# path to input file
filePath = "data.txt"

# path to output file
savePath = "{}.txt".format(SORT_TYPE)



def stoogeSort(lst, l, r):
  # if left element is larger than right element
    # swap left element and right element

  # if the length of the list is >= 3
    # call stoogeSort with inital 2/3 of list
    # call stoogeSort with last 2/3 of list
    # call stoogeSort with inital 2/3 of list agian


  # save the left most element to var left
  left = lst[l]
  # save the right most element to var right
  right = lst[r]

  # compare value of left to value of right
  if int(left) > int(right):
    # swap values in list if left is larger than right
    lst[l] = right
    lst[r] = left

  # calculat the length of values to be evaluated
  span = r - l + 1

  # test if length of values is 3 or greater
  if span >= 3:
    # calculate what 1/3 of the span
    third = span / 3

    # call stooge on first 2/3 of lst 
    stoogeSort(lst, l,  r - third)
    # call stooge on second 2/3 of lst 
    stoogeSort(lst, l + third,  r)
    # call stooge on first 2/3 of lst a second time
    stoogeSort(lst, l,  r - third)




def main():
  # get contents of input file
  fileContent = fileHandler.parseFile(filePath)

  for lst in fileContent:
    stoogeSort(lst, 0, len(lst) - 1)

  # write sorted data to output file
  fileHandler.writeFile(savePath, fileContent)
  cleanup.pyc()

if __name__ == "__main__":
  print("{}{} Sort".format(SORT_TYPE[0].upper(), SORT_TYPE[1:]))
  main()

