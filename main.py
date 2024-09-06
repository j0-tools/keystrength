import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as tkb



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
    accent_colour = ""
    entry_bg_colour = "#ffffff"
    button_colour = "#0c55cc"

    title_font = tkfont.Font(family="Gadugi", size=30, weight="bold")
    subtitle_font = tkfont.Font(family="Gadugi", size=13)
    main_font = tkfont.Font(family="Gadugi", size=12)
    result_font = tkfont.Font(family="Gadugi", size=16)
    
    style = tkb.Style()
    style.theme_use("cosmo")
    style.configure("TFrame", background=bg_colour)
    style.configure("TLabel", background=bg_colour, foreground=fg_colour, font=main_font)
    style.configure("TEntry", fieldbackground=entry_bg_colour, foreground=fg_colour, font=main_font, relief="ridge")
    style.configure("TButton", background=button_colour, foreground=fg_colour, font=main_font)
    style.map("TButton", background=[('active', accent_colour)])

    # Configure main frame
    frame = tkb.Frame(root, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
    frame.configure(border=0, relief="flat")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Header
    header_label = tkb.Label(frame, text="KeyStrength", font=title_font)
    subtitle_label = tkb.Label(frame, text="Assess the strength of your passwords at the click of a button.", font=subtitle_font, foreground="#494949")
    header_label.grid(column=0, row=0, sticky=(tk.W), padx=40, pady=5)    # Logo here? (Made space to left of header)
    subtitle_label.grid(column=0, row=1, sticky=(tk.W), padx=40)

    # Password input
    input_frame = tkb.Frame(frame)
    input_frame.grid(column=0, row=2, columnspan=3, pady=(0, 20), sticky=(tk.E, tk.W))
    password_entry = tkb.Entry(input_frame, justify="left", font=main_font, width=52)
    password_entry.grid(row=0, column=1, sticky=(tk.W), padx=40, pady=40)
    password_entry.configure(takefocus=1)
    password_entry.focus_set()


    # Event loop
    root.configure(bg=bg_colour)
    root.mainloop()








