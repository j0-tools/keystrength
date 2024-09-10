import json
import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as tkb
from ttkbootstrap import Style
from ttkbootstrap.widgets import Meter
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



### PASSWORD CHECK FUNCTIONALITY ###

class Password():
    def __init__(self, password):
        self.password = password
        self.score = 0


    # Length check (WORKING)
    def length_check(self):
        length = len(self.password)
        if length < 8:
            return 0
        elif length < 12:
            return 9
        elif length < 16:
            return 14
        else:
            return 20
    
    # Diversity check (WORKING)
    def diversity_check(self):
        
        categories = 0
        score = 0

        if any(c.islower() for c in self.password):
            categories += 1
            score += 4
        if any(c.isupper() for c in self.password):
            categories += 1
            score += 4 
        if any(c.isdigit() for c in self.password):
            categories += 1
            score += 4
        if any(c in '''!@#$%^&*()-_=+{}[];:"\'<>,.?/''' for c in self.password):
            categories += 1
            score += 8

        if categories == 4:
            score += 5

        return score
    
    # Common passwords (WORKING, BUGS)
    def common_passwords_check(self):
        with open ("data/passwords.json", "r") as file:
            common_passwords = json.load(file)

        if self.password.lower() in (word.lower() for word in common_passwords):
            return 0
        else:
            return 15
    
    # Personal info (names, movies, etc) (WORKING, BUGS)
    def common_names_check(self):
        with open("data/names.json", "r") as file:
            common_names = json.load(file)
        
        if self.password.lower() in (word.lower() for word in common_names):
            return 0
        else:
            return 15

    # Dictionary words (WORKING; BUGS)
    def dictionary_words_check(self):
        with open("data/dictionarywords.json", "r") as file:
            common_words = json.load(file)
        
        if self.password.lower() in (word.lower() for word in common_words):
            return 0
        else:
            return 15

    # Repeated characters (WORKING)
    def repeat_check(self):
        if any(self.password.count(c) > 3 for c in set(self.password)) or "abc" in self.password or "123" in self.password:
            return 0
        else:
            return 10
        
    # Entropy (randomness)
    def entropy_check(self):
        "not figured out yet"
        pass


    # Final sstrength
    def strength(self):
        self.score += self.length_check()
        self.score += self.diversity_check()
        self.score += self.common_words_check()
        self.score += self.repeat_check()
        self.score += self.consecutive_char_check()
        self.score += self.dictionary_words_check()
        self.score += self.entropy_check()


        



### GUI ###

# Main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("KeyStrength")

    # Window styling
    root.geometry("850x450")
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
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
    frame.configure(border=0, relief="flat")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Header
    header_label = tkb.Label(frame, text="KeyStrength", font=title_font)
    subtitle_label = tkb.Label(frame, text="Assess the strength of your passwords at the click of a button.", font=subtitle_font, foreground="#494949")
    header_label.grid(column=0, row=0, sticky=(tk.W), padx=38, pady=5)    # Logo here? (Made space to left of header)
    subtitle_label.grid(column=0, row=1, sticky=(tk.W), padx=39)

    # Password input
    input_frame = tkb.Frame(frame)
    input_frame.grid(column=0, row=2, columnspan=3, pady=(0, 20), sticky=(tk.E, tk.W))
    password_entry = tkb.Entry(input_frame, justify="left", font=main_font, width=55)
    password_entry.grid(row=0, column=1, sticky=(tk.W), padx=40, pady=20)
    password_entry.configure(takefocus=1)
    password_entry.focus_set()

    # Check strength button
    check_strength = tkb.Button(frame, text="Check", width=10)
    check_strength.grid(column=0, row=2, pady=(65, 0), padx=40, sticky=(tk.W))

    # Strength meter
    meter = tkb.Meter(frame, 
                      subtext="Strength", 
                      interactive=False, 
                      metertype="semi", 
                      stripethickness=10, 
                      bootstyle="success",    # <25="danger", <75="warning", 76-100="success"
                      amountused=95,)
    meter.grid(column=1, row=0, rowspan=3, padx=(50, 10), pady=20, sticky=(tk.S, tk.E))

    # Feedback area
    feedback_frame = tkb.Frame(frame, borderwidth=2, relief="solid", padding="60")
    feedback_frame.grid(column=0, row=4, columnspan=4, pady=10, padx=39, sticky=(tk.W, tk.E, tk.N, tk.S))
    feedback = tkb.Label(feedback_frame, font=main_font)
    feedback.grid(row=3, column=0, columnspan=4)

    # Layout
    root.columnconfigure(1, weight=1)

    # Event loop
    root.configure(bg=bg_colour)
    root.mainloop()








