#Annemarie McDonnell
with open("data/iris.csv")as f:
 contents=f.read()
 print(contents)
for line in f:
    a = line.split(',')
    print (a[0], a[1], a[2], a[3])





        

        
