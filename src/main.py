import json
from tkinter import *

finalPlacement = {"row": 4, "column": 0, "columnspan": 2}
theFont = ("Arial", 20)
sType = None

def price_calc(type, height, width):
    with open(f'.\prices\{type}.json', 'r') as file:
        ball = json.load(file)
        try:
            thecool = ball[str(height)][0][str(width)]
            if type == "Domestic": finalPrice = (thecool * 1.2 + 427.5)
            else: finalPrice = ((thecool * 1.1 * 1.3 + 571) * 1.1)
            finalPrice = "{:.2f}".format(finalPrice)
            priceLabel.config(text=f"Price: ${finalPrice}", font=theFont)
            priceLabel.grid(finalPlacement)
        except KeyError: ValueerrorLabel.grid(finalPlacement)

def calculate():
    ValueerrorLabel.grid_forget()
    priceLabel.grid_forget()

    try: 
        if sType == "EasyView": width = int(widthEntry.get()) + 140
        elif sType == "55mm": width = int(widthEntry.get()) + 140
        elif sType == "77mm": width = int(widthEntry.get()) + 220
        elif sType == "36mm": width = int(widthEntry.get()) + 140
        elif sType == "Domestic": width = int(widthEntry.get()) + 120
    except ValueError: ValueerrorLabel.grid(finalPlacement)

    try:
        if sType == "EasyView": height = int(heightEntry.get()) + 250
        elif sType == "55mm": height = int(heightEntry.get()) + 250
        elif sType == "77mm": height = int(heightEntry.get()) + 300
        elif sType == "36mm": height = int(heightEntry.get()) + 250
        elif sType == "Domestic": height = int(heightEntry.get()) + 205
    except ValueError: ValueerrorLabel.grid(finalPlacement)

    if width % 100 != 0: width = width + (100 - (width % 100))
    if height % 100 != 0: height = height + (100 - (height % 100))

    price_calc(sType, height, width)




# create a tkinter gui
root = Tk()
root.title("Shutter Price Calculator")

# END LABELS
ValueerrorLabel = Label(root, text="Out of engineered range! Contact 1800 748 887", font=theFont, fg="red")
priceLabel = Label(root, text="", font=theFont, fg="green")

# Normal Labels
Label(root, text="Height: ", font=theFont).grid(row=0, column=0, sticky='e')
Label(root, text="Width: ", font=theFont).grid(row=1, column=0, sticky='e')

# Entries
widthEntry = Entry(root, font=theFont)
widthEntry.grid(row=0, column=1, pady=("10", "0"), padx=("0", "10"))
heightEntry = Entry(root, font=theFont)
heightEntry.grid(row=1, column=1, pady=("0", "10"), padx=("0", "10"))

# create a button
def change(shutter):global sType;sType = shutter
change("Domestic")
options = ["Domestic", "55mm", "77mm", "EasyView", "36mm"]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options, command=change)
drop.config(font=theFont)
drop.grid(row=2, column=0, columnspan=2, sticky='nesw', padx=10)
Button(root, text="Calculate", font=theFont, command=calculate).grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky='nesw')

# run the gui
root.mainloop()
