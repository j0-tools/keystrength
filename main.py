import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as tkb



###################
### KEYSTRENGTH ### 
###################



### CLI FIRST RUN ###

# Welcome message 
print("\n\n### KeyStrength Password Checker ###")

value = True

# Main loop
while value == True:
    
    # Prompt for password
    pw = input("\nType a password: ")
    length = len(pw)
    
    # Check if password empty
    if pw == "":
        print("Password cannot be empty.\n")
        continue
    
    # Length check
    if length < 8:
        print("Password is very weak.\nPassword needs more characters.\n")
    elif length < 12:
        print("Password is weak.\nPassword needs more characters.\n")
    elif length < 16:
        print("Password is moderate.\nTo strengthen, try using a password more than 15 characters in length.\n")
    else:
        print("Password is strong.\nWell done!\n")

    # Continue?
    yn = input("Try another password? (Y/N): ")
    if yn.upper() == "Y":
        continue
    else:
        break

print("\nThanks for using KeyStrength!")









