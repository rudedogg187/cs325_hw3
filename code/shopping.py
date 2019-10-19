# CS325 OSU
# INSERT SORT
# ASSIGNMENT 3
# 21 OCT 2019
##################
#ref: 	



import fileHandler
import cleanup
import mergesort



# type of sorting method, also output file name
NAME = "shopping"


# path to input file
filePath = "shopping.txt"

# path to output file
savePath = "{}.txt".format(NAME)


def buildMatrix(width, height):
  matrix = [[-1 for x in range(width)] for y in range(height)]
  return matrix


def knapShop(max_weight, matrix, item_lst):
  n = len(item_lst) - 1
  m = max_weight

 # n = 1
 # m = 2

  # iterate through all of the items
  for i in range(0, n + 1):

    # iterate through all of the weights
    for w in range(0, m + 1):
      item_wgt = item_lst[i]["weight"]
      item_val = item_lst[i]["price"]
      above_val = matrix[i - 1][w]
      #print "i: {},  w: {}, wgt: {}, val: {}".format(i, w, item_wgt, item_val)


      # case 1 - base case, zero out first row and first col in matrix
      if i == 0 or w == 0:
        matrix[i][w] = 0

      elif item_wgt <= w:
        new_val = matrix[i - 1][w - item_wgt]
        new_val += item_val

        max_val = max(above_val, new_val)
        
        matrix[i][w] = max_val

      else:
        matrix[i][w] = above_val


  #for row in matrix:
    #print row


  
def getItems(max_weight, matrix, item_lst):
  n = len(item_lst) - 1
  m = max_weight

  i = n
  w = m

  total_wgt = 0
  total_val = 0

  while i > 0: # and w > 0:
    cell_val = matrix[i][w]
    above_val = matrix[i - 1][w]
    item_wgt = item_lst[i]["weight"]
    item_val = item_lst[i]["price"]

    if cell_val != above_val:
      print "Item {} ({}lbs) WAS used (${}.00)".format(i, item_wgt, item_val)
      total_wgt += item_wgt
      total_val += item_val
      w -= item_wgt
    
    '''
    else:
      print "Item {} WAS NOT used".format(i)
    '''

    i -= 1
   
  print "_______"
  print "\t({}lbs)\t${}.00".format(total_wgt, total_val) 

  '''
  for row in matrix:
    print row

  print matrix[i][w]
  '''
  


def maximizeShopping(item_lst, family_lst):
  # sort family list, this is to make sure the we can get the greatest weight
  mergesort.mergeSort(family_lst, 0, len(family_lst) - 1)

  #add a 0 weight, 0 value item to the start of the item lst
  item_lst = [{"price": 0, "weight": 0}] + item_lst

  # build a table to house 0 to max weight of family by 0 item count
  matrix = buildMatrix(family_lst[-1] + 1, len(item_lst))

  # iterate through family members, exlude fist member because this always has aweight of zero
  for i in range(0, len(family_lst)):#[-1:]:
    member_weight = family_lst[i]
    knapShop(member_weight, matrix, item_lst)
    getItems(member_weight, matrix, item_lst)





def main():
  # get contents of input file
  fileContent = fileHandler.parseShopping(filePath)

  for test in fileContent:#[1:2]:
    item_lst = test["item_lst"]
    family_lst = test["family_lst"]
    ###### TEST TEST TEST
    '''
    item_lst = [
      {"price": 1, "weight": 2},
      {"price": 2, "weight": 3},
      {"price": 5, "weight": 4},
      {"price": 6, "weight": 5}
    ]

    family_lst = [8]
    '''
    ###### TEST TEST TEST
    maximizeShopping(item_lst, family_lst)

  

  # write data to output file
  #fileHandler.writeFile(savePath, fileContent)
  cleanup.pyc()


if __name__ == "__main__":
  print("{}{} Sort".format(NAME[0].upper(), NAME[1:]))
  main()

