# CS325 OSU
# SHOPPING SPREE
# ASSIGNMENT 3
# 21 OCT 2019
##################
#ref: 	



###########################################
# MODULES
###########################################
import fileHandler
import cleanup



###########################################
# CONSTS AND VARS
###########################################
# name of algorithm
NAME = "shopping"


# path to input file
filePath = "shopping.txt"

# path to output file
savePath = "result.txt"



#############################################
# FUNCTION -- PRINT MATRIX (FOR TESTING)
# Takes a matrix as params
# Prints a matrix for testing purposes 
############################################## 
def printMatrix(matrix):
  print "-" * 100
  for row in matrix:
    row_text = "\t"
    for col in row:
      row_text += "{} \t".format(col)
    row_text += "\n"
    print row_text

  print "-" * 100


#############################################
# FUNCTION -- GET A LIST'S MAX VALUE'S INDEX
# Takes a list as params
# Returns the index of the max value in list 
############################################## 
def lstMax(lst):
  mx = 0
  for i in range(1, len(lst)):
    if lst[i] > lst[mx]:
      mx = i
  return mx



#############################################
# FUNCTION -- BUILD A NESTED LIST (MATRIX)
# Takes width and height as params
# Returns matrix with all values init'd to -1 
##############################################
def buildMatrix(width, height):
  matrix = [[-1 for x in range(width)] for y in range(height)]
  return matrix



#############################################
# FUNCTION -- FILL IN A MATRIX WITH ITEM VALUES
# Takes max carry capacity, matrix and list of items as params
# Fills in cells of matrix that are -1
##############################################
def memberSpree(max_weight, matrix, item_lst):
  n = len(item_lst) - 1			#max item index
  m = max_weight			#max weight index

  if matrix[n][m] == -1:

    # HERE ONLY IF MATRIX HAS NOT BEEN FILLED TO NEEDED COLUMN
    # iterate through all of the items
    for i in range(0, n + 1):

      # iterate through all of the weights
      for w in range(0, m + 1):

        #check if current matrix cell has been calculated by lower family member
        # HERE ONLY IF MATRIX CELL HAS NOT BEEN ALREADY FILLED
        if matrix[i][w] == -1:
          item_wgt = item_lst[i]["weight"]	#item to evaluate's weight 
          item_val = item_lst[i]["price"]		#item to evaluate's price
          prev_val = matrix[i - 1][w]		#value directly above current cell
     
          # case 1 - base case, zero out first row and first col in matrix
          if i == 0 or w == 0:
            matrix[i][w] = 0

          # case 2 - item being evaluated is less than person's carrying capacity
          elif item_wgt <= w:
            new_val = matrix[i - 1][w - item_wgt]	  #go up row and back items weight (wgt w/o last item)
            new_val += item_val			  #add weight of item being evaluated to this value

            max_val = max(prev_val, new_val)	  #compare prev/curr val to val if new item 
        
            matrix[i][w] = max_val		  #set the matrix cell to the max of comparison

          # case 3 - since item was too heavy, cell's val equals the prev/curr val
          else:
            matrix[i][w] = prev_val

  return getItems(max_weight, matrix, item_lst)

  #printMatrix(matrix)



def getItems(max_weight, matrix, item_lst):
  n = len(item_lst) - 1
  m = max_weight

  i = n
  w = m

  total_wgt = 0
  total_val = 0

  items = []

  while i > 0 and w > 0:
    cell_val = matrix[i][w]
    above_val = matrix[i - 1][w]
    item_wgt = item_lst[i]["weight"]
    item_val = item_lst[i]["price"]

    if cell_val != above_val:
      total_wgt += item_wgt
      total_val += item_val
      w -= item_wgt

      items.append(i) 
    
    i -= 1

  return { "val": total_val, "items": items }

  


def familySpree(item_lst, family_lst):
  #add a 0 weight, 0 value item to the start of the item lst
  item_lst = [{"price": 0, "weight": 0}] + item_lst

  # get the index of the highest capacity family member
  max_i = lstMax(family_lst)
  
  # build a matrix to house 0 to max weight of family by 0 item count
  matrix = buildMatrix(family_lst[max_i] + 1, len(item_lst))

  family_val = 0
  member_items = []

  # iterate through family members, exclude first member because this always has a weight of zero
  for i in range(0, len(family_lst)):#[-1:]:
    member_max_weight = family_lst[i]
    result = memberSpree(member_max_weight, matrix, item_lst)
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



def main():
  # get contents of input file
  fileContent = fileHandler.parseShopping(filePath)

  t = 1
  test_results = []
  for test in fileContent[0:20]:
    item_lst = test["item_lst"]
    family_lst = test["family_lst"]
    result = familySpree(item_lst, family_lst)
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
  main()

