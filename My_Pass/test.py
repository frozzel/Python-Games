# try:
#     file = open('test.txt', 'r')
#     print(file.read())
# except FileNotFoundError:
#     file = open('test.txt', 'w')
#     print('File created')
# except PermissionError:
#     print('Permission denied')
# except Exception as e:
#     print('Unknown error:', e)
# except IndexError:
#     print('Index error')
# else:
#     print('File read successfully')
# finally:
#     file.close()
#     print('File closed')
#     print('End of program')
#     # raise Exception('This is an exception')
    
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
try:
    def make_pie(index):
        fruit = fruits[index]
        print(fruit + " pie")

    make_pie(1)
except IndexError:
    print("Fruit pie")
except KeyError:
    print("Fruit pie")
finally:
    print("Fruit pie")