list = ["hello", " ", "world"]
npImgsFileName = "testtxt.txt"

file = open(npImgsFileName, "w")
file.writelines(list)
file.close()