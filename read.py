f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()



f = open("demo.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)


f.close()