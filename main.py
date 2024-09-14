import math
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



    ### CHECKS ###

    # Length check
    def length_check(self):
        length = len(self.password)
        if length < 8:
            return -20
        elif length < 11:
            return 5
        elif length < 13:
            return 8
        elif length < 15:
            return 12
        elif length < 17:
            return 15
        elif length < 19:
            return 20
        elif length < 22:
            return 25
        elif length < 24:
            return 30
        elif length < 28:
            return 35
        else:
            return 40
    
    # Diversity check
    def diversity_check(self):
        
        categories = 0
        score = 0

        if any(c.islower() for c in self.password):
            categories += 1
        if any(c.isupper() for c in self.password):
            categories += 1
        if any(c.isdigit() for c in self.password):
            categories += 1
        if any(c in '''!@#$%^&*()-_=+{}[];:"\'<>,.?/''' for c in self.password):
            categories += 1

        score = categories * 3
        if categories == 4:
            score += 15

        return score
    
    # Common passwords
    def common_passwords_check(self):
        if len (self.password) >= 223:
            return 5
        if len (self.password) >= 18:
            return 3
        else:
            try:
                with open ("data/passwords.json", "r") as file:
                    common_passwords = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading common passwords list: {e}")
                return 0

            password_lower = self.password.lower()

            if any(word.lower() in password_lower for word in common_passwords):
                return -20
            else:
                return 10
    
    # Personal info (names, movies, etc)
    def common_names_check(self):
        if len (self.password) >= 18:
            return 5
        else:
            try:
                with open("data/names.json", "r") as file:
                    common_names = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading common names list: {e}")
                return 0
            
            password_lower = self.password.lower()
            
            if any(name.lower() in password_lower for name in common_names):
                return -5
            else:
                return 5

    # Dictionary words
    def dictionary_words_check(self):
        if len (self.password) >= 18:
            return 5
        else:
            try:
                with open("data/dictionarywords.json", "r") as file:
                    common_words = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading dictionary words list: {e}")
                return 0

            longer_words = [word for word in common_words if len(word) >= 3]
            
            if any(word in self.password for word in longer_words):
                return -5
            else:
                return 5

    # Repeated characters
    def repeat_check(self):
        
        password_lower = self.password.lower()
        common = [
        # Alphabetic
        "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij",
        "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr",
        "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz",
        # Reverse
        "zyx", "yxw", "xwv", "wvu", "vut", "uts",
        # Numeric
        "123", "234", "345", "456", "567", "678", "789", "890",
        # Reverse numeric
        "987", "876", "765", "654", "543", "432", "321",
        # Keyboard patterns
        "qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop",
        "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl",
        "zxc", "xcv", "cvb", "vbn", "bnm",
        # Keyboard patterns (AZERTY)
        "aze", "zer", "ert", "rty", "tyu", "yui", "uio", "iop",
        "qsd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "lm",
        "wxc", "xcv", "cvb", "vbn",
        # Common substitutions
        "!@#", "@#$", "#$%", "$%^", "%^&", "^&*", "&*(", "*()"]

        if any(password_lower.count(c) > 2 for c in set(password_lower)):
            return -3
        elif any(seq in password_lower for seq in common):
            return -3
        else:
            return 8
        
    # Entropy (randomness)
    def entropy_check(self):
        char_set = set(self.password)
        entropy = len(self.password) * math.log2(len(char_set))

        if entropy < 5:
            return -50
        elif entropy < 45:
            return 0
        elif entropy < 55:
            return 8
        elif entropy < 70:
            return 15
        elif entropy < 85:
            return 22
        elif entropy < 105:
            return 28
        else:
            return 35



    ### FINAL STRENGTH ###

    def strength(self):
        self.score = (
            self.length_check() +
            self.diversity_check() +
            self.common_passwords_check() +
            self.common_names_check() +
            self.dictionary_words_check() +
            self.repeat_check() +
            self.entropy_check() 
        )
        if self.score >= 50:
            self.score += 5
        if len(self.password) > 30:
            self.score += 5
        return max(1, min(100, self.score))    # 1-100



        
### GUI ###

# Main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("KeyStrength")

    # Window styling
    root.geometry("850x300")
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
    subtitle_label = tkb.Label(frame, text="Assess the strength of your passwords.                                   ", font=subtitle_font, foreground="#494949")
    header_label.grid(column=0, row=0, sticky=(tk.W), padx=38, pady=5)    # Logo here? (Made space to left of header)
    subtitle_label.grid(column=0, row=1, sticky=(tk.W), padx=39)

    # Password input
    input_frame = tkb.Frame(frame)
    input_frame.grid(column=0, row=2, columnspan=3, pady=(0, 20), sticky=(tk.E, tk.W))

    # Live checking
    password_var = tk.StringVar()
    password_entry = tkb.Entry(input_frame, textvariable=password_var, justify="left", font=main_font, width=55)
    password_entry.grid(row=0, column=1, sticky=(tk.W), padx=40, pady=20)
    password_entry.configure(takefocus=1)
    password_entry.focus_set()

    def password_check(*args):
        password = password_var.get()
        if len(password) <= 5:
            meter.configure(amountused=1, bootstyle="danger")
        elif len(password) >= 8:
            check = Password(password)
            score = check.strength()
            meter.configure(amountused=score)

            if score <= 25:
                meter.configure(bootstyle="danger")
            elif score <= 75:
                meter.configure(bootstyle="warning")
            else:
                meter.configure(bootstyle="success")
        
        else:
            meter.configure(amountused=1, bootstyle="danger")

    password_var.trace_add("write", password_check)

    # Strength meter
    meter = tkb.Meter(frame, 
                      subtext="Strength", 
                      interactive=False, 
                      metertype="semi", 
                      stripethickness=10, 
                      bootstyle="",  
                      amountused=0,)
    meter.grid(column=1, row=0, rowspan=3, padx=(50, 10), pady=20, sticky=(tk.S, tk.E))

    # Layout
    root.columnconfigure(1, weight=1)

    # Binds

    # Event loop
    root.configure(bg=bg_colour)
    root.mainloop()








