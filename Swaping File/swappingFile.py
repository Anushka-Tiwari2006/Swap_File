def swapFileData():
    input("Name of the file you want to swap:-")
    input("Name of the file you want to swap with:-")

with open("file1.txt","r") as a:
     data_a = a.read()
     
with open("file2.txt","r") as a:
     data_b = a.read()
     
with open("file1.txt","w") as a:
     a.write(data_b)
     
with open("file2.txt","w") as a:
     a.write(data_a)
         
swapFileData()