# type of sorting method, also output file name
SORT_TYPE = "shopping"

# read input file and parse it to pull out the arrays to be sorted
def parseFile(filePath):
  with open(filePath) as f:
    raw = f.readlines()

  ret = []
  for row in raw:
    lst = row.replace("\n", "").strip().split(" ")
    if len(lst) > 1:
      ret.append(lst[1:])

  return ret



# write the sorted arrays back to SORT_TYPE.txt
def writeFile(savePath, fileContent):
  raw = ""
  for row in fileContent:
    raw += " ".join(row) + "\n"

  with open(savePath, "w+") as f:
    f.write(raw)


def parseShoppingx(filePath):
  with open(filePath) as f:
    raw = f.readlines()
     
  t = int(raw[0].replace("\n", "")) #number of tests
  test_lst = []

  raw = raw[1:]

  while t > 0:
    params = {}
    item_ct = int(raw[0].replace("\n", "")) #number of items
    params["item_ct"] = item_ct
    raw = raw[1:]

    item_lst = raw[:item_ct]
    params["item_lst"] = []
    for i in range(0, len(item_lst)):
      item = {}

      splt = item_lst[i].split(" ")

      item["price"] = int(splt[0])
      item["weight"] = int(splt[1].replace("\n", ""))

      params["item_lst"].append(item)

    raw = raw[item_ct:]

    family_ct = int(raw[0].replace("\n", "")) #number of members
    params["family_ct"] = family_ct
    raw = raw[1:]

    family_lst = raw[:family_ct]
    for i in range(0, len(family_lst)):
      family_lst[i] = int(family_lst[i].replace("\n", ""))

    params["family_lst"] = family_lst
    raw = raw[family_ct:]
	
    t -= 1

    test_lst.append(params)


  return test_lst

  


def parseShopping(filePath):
  with open(filePath) as f:
    raw = f.readlines()
     
  t = int(raw[0].replace("\n", "")) #number of tests
  test_lst = []

  raw = raw[1:]

  while t > 0:
    params = {}
    item_ct = int(raw[0].replace("\n", "")) #number of items
    params["item_ct"] = item_ct
    raw = raw[1:]

    item_lst = raw[:item_ct]
    params["item_lst"] = [] #[{"price": 0, "weight": 0}]
    for i in range(0, len(item_lst)):
      item = {}

      splt = item_lst[i].split(" ")

      item["price"] = int(splt[0])
      item["weight"] = int(splt[1].replace("\n", ""))

      params["item_lst"].append(item)

    raw = raw[item_ct:]

    family_ct = int(raw[0].replace("\n", "")) #number of members
    params["family_ct"] = family_ct
    raw = raw[1:]

    family_lst = raw[:family_ct]
    for i in range(0, len(family_lst)):
      family_lst[i] = int(family_lst[i].replace("\n", ""))


    params["family_lst"] = family_lst
    #params["family_lst"].append(0)

    raw = raw[family_ct:]
	
    t -= 1

    test_lst.append(params)

  return test_lst

  


    
      



# path to input file
filePath = "data.txt"
# path to output file
savePath = "{}.txt".format(SORT_TYPE)


shoppingFile = "shopping.txt"


def main():
  # get contents of input file
  fileContent = parseShopping(shoppingFile)
  print fileContent[0]
  # write sorted data to output file
  #writeFile(savePath, fileContent)

if __name__ == "__main__":
#  print("{}{} Sort".format(SORT_TYPE[0].upper(), SORT_TYPE[1:]))
  main()

