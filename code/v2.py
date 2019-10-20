# CS325 OSU
# SHOPPING SPREE
# ASSIGNMENT 3
# 21 OCT 2019
##################
#ref: 	



import fileHandler
import cleanup


# name of algorithm
NAME = "shopping"


# path to input file
filePath = "shopping.txt"

# path to output file
savePath = "result.txt"

def lstMax(lst):
  mx = 0
  for i in range(1, len(lst)):
    if lst[i] > lst[mx]:
      mx = i
  return mx



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

  items = []

  while i > 0: # and w > 0:
    cell_val = matrix[i][w]
    above_val = matrix[i - 1][w]
    item_wgt = item_lst[i]["weight"]
    item_val = item_lst[i]["price"]

    if cell_val != above_val:
      #print "Item {} ({}lbs) WAS used (${}.00)".format(i, item_wgt, item_val)
      total_wgt += item_wgt
      total_val += item_val
      w -= item_wgt

      items.append(i) 
    
    i -= 1

  return { "val": total_val, "items": items }
   
  #print "_______"
  #print "\t({}lbs)\t${}.00".format(total_wgt, total_val) 


  '''
  for row in matrix:
    print row

  print matrix[i][w]
  '''
  


def maximizeShopping(item_lst, family_lst):
  #add a 0 weight, 0 value item to the start of the item lst
  item_lst = [{"price": 0, "weight": 0}] + item_lst

  # get the index of the highest capacity family member
  max_i = lstMax(family_lst)
  
  # build a table to house 0 to max weight of family by 0 item count
  matrix = buildMatrix(family_lst[max_i] + 1, len(item_lst))

  # iterate through family members, exlude fist member because this always has aweight of zero
  family_val = 0
  member_items = []
  for i in range(0, len(family_lst)):#[-1:]:
    member_weight = family_lst[i]
    knapShop(member_weight, matrix, item_lst)
    result = getItems(member_weight, matrix, item_lst)
    family_val += result["val"]
    member_items.append(result["items"])


  return { "family_val": family_val, "member_items": member_items }

def buildResultString(test_results):
  result_string = ""
  for test in test_results:
    result_string += "Test Case {}\n".format(test["case"])
    result_string += "Total Price {}\n".format(test["family_val"])
    result_string += "Member Items:\n"

    for m in range(0, len(test["member_items"])):
      items = test["member_items"][m]
      result_string += "{}: ".format(m + 1)
      for i in range(0, len(items)):
        result_string += "{} ".format(items[len(items) -1 -i])

      result_string += '\n'

    result_string += "\n"

  return result_string[:-2]


########################################################################
def printMatrix(matrix):
  for row in matrix:
    row_text = ""
    for col in row:
      row_text 
      row_text += "{}\t".format(col)

    row_text += "\n"
    print row_text




#def memberSpree(m, item_lst, matrix):


def familySpree(item_lst, family_lst, t):
  #add a 0 weight, 0 value item to the start of the item lst
  item_lst = [{"price": 0, "weight": 0}] + item_lst

  max_cap_i = lstMax(family_lst)
  matrix_width = family_lst[max_cap_i] + 1
  matrix_height = len(item_lst)

  matrix = [[-1 for x in range(matrix_width)] for y in range(matrix_height)]

  for m in family_lst[0:1]:
    print m





def recursive():
  # get contents of input file
  fileContent = fileHandler.parseShopping(filePath)

  t = 1
  for test in fileContent[0:1]:
    item_lst = test["item_lst"]
    family_lst = test["family_lst"]
    familySpree(item_lst, family_lst, t)

    t += 1

########################################################################

def main():
  # get contents of input file
  fileContent = fileHandler.parseShopping(filePath)

  t = 1
  test_results = []
  for test in fileContent[0:20]:
    item_lst = test["item_lst"]
    family_lst = test["family_lst"]
    result = maximizeShopping(item_lst, family_lst)
    result["case"] = t 
    test_results.append(result)

    t += 1

  result_string = buildResultString(test_results)

  print result_string

  # write data to output file
  fileHandler.writeShopping(savePath, result_string)
  cleanup.pyc()


if __name__ == "__main__":
  print("{}{} Spree".format(NAME[0].upper(), NAME[1:]))
  recursive()

