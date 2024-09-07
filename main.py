import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as tkb
from PIL import Image
Image.CUBIC = Image.BICUBIC




###################
### KEYSTRENGTH ### 
###################



### CLI FIRST RUN ###


# Test loop
def console_check():

    print("\n\n### KeyStrength Password Checker ###")

    while True:
        
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

#console_check()



### GUI ###

# Main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("KeyStrength")

    # Window styling
    root.geometry("800x400")
    root.resizable(False, False)

    # Styling
    bg_colour = "#f3f3f3"
    fg_colour = "#191919"
    accent_colour = "#f3f3f3"
    entry_bg_colour = "#ffffff"
    button_colour = "#0f6aff"
    button_hover_colour = "#0c55cc"

    title_font = tkfont.Font(family="Gadugi", size=30, weight="bold")
    subtitle_font = tkfont.Font(family="Gadugi", size=13)
    main_font = tkfont.Font(family="Gadugi", size=12)
    result_font = tkfont.Font(family="Gadugi", size=16)
    
    style = tkb.Style()
    style.theme_use("cosmo")
    style.configure("TFrame", background=bg_colour)
    style.configure("TLabel", background=bg_colour, foreground=fg_colour, font=main_font)
    style.configure("TEntry", fieldbackground=entry_bg_colour, foreground=fg_colour, font=main_font, relief="ridge")
    style.configure("TButton", background=button_colour, foreground=accent_colour, font=main_font)
    style.map("TButton", background=[('active', button_hover_colour)])

    # Configure main frame
    frame = tkb.Frame(root, padding="10")
    frame.pack(fill="both", expand=True, padx=10, pady=10)    # Converted to a pack layout.
    frame.configure(border=0, relief="flat")

    # Header
    header_label = tkb.Label(frame, text="KeyStrength", font=title_font)
    subtitle_label = tkb.Label(frame, text="Assess the strength of your passwords at the click of a button.", font=subtitle_font, foreground="#494949")
    header_label.pack(anchor=(tk.W), padx=38, pady=5)    # Logo here? (Made space to left of header)
    subtitle_label.pack(anchor=(tk.W), padx=39)

    # Password input
    input_frame = tkb.Frame(frame)
    input_frame.pack(fill="x", pady=(0, 20), padx=40)

    password_entry = tkb.Entry(input_frame, justify="left", font=main_font, width=58)
    password_entry.pack(side="left", pady=20)
    password_entry.configure(takefocus=1)
    password_entry.focus_set()

    # Check strength button
    button_frame = tkb.Frame(frame)
    button_frame.pack(pady=(0, 20), padx=40)

    check_strength = tkb.Button(button_frame, text="Check", width=10)
    check_strength.pack(padx=300)


    # Event loop
    root.configure(bg=bg_colour)
    root.mainloop()








