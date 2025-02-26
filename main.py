
file = open("practise.txt", "r")
print(file.read())
file.close()


file = open("practise.txt", "a")
file.write("This is a new line in the file\n")
file.close()

file = open("practise.txt", "r")
print(file.read())
file.close()

# Tries to open the file and if it doesn't exist it will create it
try:
    file = open("names.txt", "r")
    print(file.read())
    file.close()
except:
    file = open("names.txt", "w")
    file.write("This file will contain names\n")
    file.close()