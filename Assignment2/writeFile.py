# Write a file
f = open('myFile.txt', 'w')

f.write('Hi this is the assignment2.\nDoing the exercise for the devOps')
f.close()

#Read a file
f = open('myFile.txt', 'r')

data = f.read()
print(data)
f.close()
