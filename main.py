import json
from tkinter import *

def calculate():
    # remove all the error labels
    widthminError.grid_forget()
    widthmaxError.grid_forget()
    heightminError.grid_forget()
    heightmaxError.grid_forget()
    ValueerrorLabel.grid_forget()
    priceLabel.grid_forget()

    try: width = int(widthEntry.get())
    except ValueError: ValueerrorLabel.grid(row=3, column=0, columnspan=2); return
    if width < 600: widthminError.grid(row=3, column=0, columnspan=2); return
    elif width > 3000: widthmaxError.grid(row=3, column=0, columnspan=2); return

    try: height = int(heightEntry.get())
    except ValueError: ValueerrorLabel.grid(row=3, column=0, columnspan=2); return
    if height < 600: heightminError.grid(row=3, column=0, columnspan=2); return
    elif height > 3500: heightmaxError.grid(row=3, column=0, columnspan=2); return

    if width % 100 != 0: width = width + (100 - (width % 100))
    if height % 100 != 0: height = height + (100 - (height % 100))

    with open('list.json', 'r') as file:
        ball = json.load(file)
        thecool = ball[str(width)][0][str(height)]
        finalPrice = (thecool * 1.3 + 455) * 1.1

        finalPrice = "{:.2f}".format(finalPrice)
        priceLabel.config(text=f"Price: ${finalPrice}", font=("Arial", 20))
        priceLabel.grid(row=3, column=0, columnspan=2)

# create a tkinter gui
root = Tk()
root.title("Shutter Price Calculator")

# END LABELS
ValueerrorLabel = Label(root, text="Please enter a number.", font=("Arial", 20), fg="red")
widthminError = Label(root, text="Width must be at least 600mm", font=("Arial", 20), fg="red")
widthmaxError = Label(root, text="Width cannot exceed 3000mm", font=("Arial", 20), fg="red")
heightminError = Label(root, text="Height must be at least 600mm", font=("Arial", 20), fg="red")
heightmaxError = Label(root, text="Height cannot exceed 3500mm", font=("Arial", 20), fg="red")
priceLabel = Label(root, text="", font=("Arial", 20), fg="green")

# Normal Labels
Label(root, text="Width: ", font=("Arial", 20)).grid(row=0, column=0, sticky='w', padx=10)
Label(root, text="Height: ", font=("Arial", 20)).grid(row=1, column=0, sticky='w', padx=10)

# Entries
widthEntry = Entry(root, font=("Arial", 20))
widthEntry.grid(row=0, column=1, padx=10)
heightEntry = Entry(root, font=("Arial", 20))
heightEntry.grid(row=1, column=1, padx=10)

# create a button
Button(root, text="Calculate", font=("Arial", 20), command=calculate).grid(row=2, column=1, columnspan=2, pady=10)

# run the gui
root.mainloop()
