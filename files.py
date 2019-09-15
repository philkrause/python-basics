# Python has functions for creating, reading, updating, and deleting files.

#To open/create a file

myFile = open('myfile.txt', 'w')


#Get info on file

print('Name:', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)


#Write to file
myFile.write('I love python')
myFile.write(' and JS')
myFile.close()

#Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like TS')
myFile.close()


#Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)