import tkinter as tk
window = tk.Tk()
window.title("Fahrenheit to Celcius Converter")
frame = tk.Frame(master=window)
frame.grid(row=0, column=0)

window.geometry("800x500")


fahrenheit = tk.Entry(master=frame, width=20)
def convert():    
    fah = float(fahrenheit.get())
    celsius = ((5/9) * fah) - 32
    print(celsius)
    label_results['text'] = round(celsius, 2), "\N{DEGREE CELSIUS}"


fahrenheit.grid(row=1, column=0)
labelFah = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}").grid(row=1, column=1)
button = tk.Button(master=frame, text="Convert", command=convert).grid(row=1, column=2)
# displayed_results = tk.Label(master=frame).grid(row=1, column=3)
label_results = tk.Label(master=frame, text="\N{DEGREE CELSIUS}")
label_results.grid(row=1, column=3)


window.mainloop()