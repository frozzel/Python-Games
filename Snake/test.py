file = open('myfile.txt')
print(file.read())
file.close()

with open("myfile.txt", "r") as data:
    contents = data.read()
    print(contents)
    
with open("myfile.txt", "a") as data:
    data.write("\nNew text.")
 
with open("../Hangman/death.txt", "r") as data:
    contents = data.read()
    print(contents)