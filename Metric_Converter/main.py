import tkinter as tk

window = tk.Tk()
window.title("Metric Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

result_label = tk.Label(text="0")
result_label.grid(column=1, row=1)

input = tk.Entry(width=10)
input.grid(column=1, row=0)

mile_label = tk.Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

convert_label = tk.Label(text="Convert")
convert_label.grid(column=0, row=0)

def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.60934)
    result_label.config(text=f"{km}")

        
button = tk.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()