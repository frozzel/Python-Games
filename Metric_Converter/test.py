import tkinter as tk

window = tk.Tk()
window.title("Metric Converter")
window.minsize(width=800, height=600)

my_label = tk.Label(text="Enter a value to convert:", font=("Arial", 24, "bold"),)
my_label.pack()

counter = 0 

def button_clicked():
    global counter
    counter += 1
    my_label["text"] = "Button was clicked " + str(counter) + " times"
    
    print(input.get())
    # my_label["text"] = input.get() + " THis is the input"
    
button = tk.Button(text="Click Me", command=button_clicked)

button.pack()

input = tk.Entry(width=10)
input.pack()

def add(*args):
    print(args)
    sum = 0
    for arg in args:
        sum += arg
    print(sum)
    
# add(1, 2, 3, 4, 5)

def multiply(*args):
    print(args)
    product = 1
    for arg in args:
        product *= arg
    print(product)

# multiply(6, 2, 4)



window.mainloop()