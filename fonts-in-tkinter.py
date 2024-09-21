from tkinter import Tk, font
root = Tk()
root.withdraw()

fonts = [f.lower() for f in font.families()]

while True:
    text = input("Enter the font you're looking for: ").lower()
    if text in fonts:
        print(f"'{text}' CAN be used with Tkinter.\n")
    else:
        print(f"'{text}' CANNOT be used with Tkinter.\n")



