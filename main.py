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

    ### LOAD DATA INTO MEMORY ###

    common_passwords = set()
    common_names = set()
    dictionary_words = set()

    @classmethod
    def load_dictionaries(cls):
        try:
            with open("data/passwords.json", "r") as file:
                cls.common_passwords = set(json.load(file))
            with open("data/names.json", "r") as file:
                cls.common_names = set(json.load(file))
            with open("data/dictionarywords.json", "r") as file:
                cls.dictionary_words = set(json.load(file))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading dictionaries: {e}")


    def __init__(self, password):
        self.password = password
        self.score = 0
        if not Password.common_passwords:    # Lazy?
            Password.load_dictionaries



    ### CHECKS ###

    # Length check
    def length_check(self):
        length = len(self.password)
        if length < 8:
            return -99
        elif length < 10:
            return 0
        elif length < 12:
            return 10
        elif length < 14:
            return 15
        elif length < 16:
            return 19
        elif length < 18:
            return 27
        elif length < 20:
            return 30
        else:
            return 35
    
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

        score = categories * 5
        if categories == 4:
            score += 10

        return score
    
    # Common passwords
    def common_passwords_check(self):
        if len (self.password) >= 16:
            return 10
        
        password_lower = self.password.lower()

        for word in self.common_passwords:
            if word.lower() == password_lower:    # Exact match
                return -20
            elif word.lower() in password_lower and len(word) > len(password_lower) / 2:    # Part match
                return -10
            else:
                return 5
    
    # Personal info (names, movies, etc)
    def common_names_check(self):
        if len (self.password) >= 16:
            return 10

        password_lower = self.password.lower()
            
        if any(name.lower() in password_lower for name in self.common_names):
            return -12
        else:
            return 10

    # Dictionary words
    def dictionary_words_check(self):
        if len (self.password) >= 16:
            return 10

        longer_words = [word for word in self.dictionary_words if len(word) >= 3]
        
        if any(word in self.password for word in longer_words):
            return -12
        else:
            return 10

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
            return -10
        elif any(seq in password_lower for seq in common):
            return -10
        else:
            return 10
        
    # Entropy (randomness)
    def entropy_check(self):
        char_set = set(self.password)
        entropy = len(self.password) * math.log2(len(char_set))

        if entropy < 5:
            return -50
        elif entropy < 45:
            return 0
        elif entropy < 55:
            return 15
        elif entropy < 85:
            return 25
        else:
            return 60



    ### FINAL STRENGTH ###

    def strength(self):
        if len(self.password) < 8:
            return 1
        self.score = (
            self.length_check() +
            self.diversity_check() +
            self.common_passwords_check() +
            self.common_names_check() +
            self.dictionary_words_check() +
            self.repeat_check() +
            self.entropy_check() 
        )
        if len(self.password) > 18:
            self.score += 20
        return max(1, min(100, self.score))    # 1-100



        
### GUI ###

# Main
if __name__ == "__main__":
    Password.load_dictionaries()
    root = tk.Tk()
    root.title("KeyStrength")

    # Window styling
    root.geometry("700x235")
    root.resizable(False, False)

    # Styling
    bg_colour = "#212121"
    fg_colour = "#f3f3f3"
    accent_colour = "#f3f3f3"
    entry_bg_colour = "#212121"
    button_colour = "#00bc8c"
    button_hover_colour = "#00e6ab"

    title_font = tkfont.Font(family="Gadugi", size=30, weight="bold")
    subtitle_font = tkfont.Font(family="Gadugi", size=13)
    main_font = tkfont.Font(family="Gadugi", size=12)
    result_font = tkfont.Font(family="Gadugi", size=16)
    
    style = tkb.Style()
    style.theme_use("darkly")
    style.configure("TFrame", background=bg_colour)
    style.configure("TLabel", background=bg_colour, foreground=fg_colour, font=main_font)
    style.configure("TEntry", fieldbackground=entry_bg_colour, foreground=fg_colour, font=main_font, borderwidth=1, relief="solid")
    style.configure("Custom.TButton", background=button_colour, foreground=bg_colour, font=main_font, borderwidth=0, focuscolor=button_colour, highlightthickness=0)
    style.map("TEntry", bordercolor=[('focus', button_colour)], lightcolor=[('focus', button_colour)], darkcolor=[('focus', button_colour)])
    style.map("Custom.TButton", background=[('active', button_hover_colour)], bordercolor=[('focus', button_colour)], highlightcolor=[('focus', button_colour)])
                      
    # Configure main frame
    frame = tkb.Frame(root, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
    frame.configure(border=0, relief="flat")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Header
    header_label = tkb.Label(frame, text="KeyStrength", font=title_font, anchor="center")
    subtitle_label = tkb.Label(frame, text="Assess the strength of your passwords.", font=subtitle_font, foreground="#9c9c9c")
    header_label.grid(column=0, row=0, columnspan=2, sticky=(tk.W), padx=38, pady=(0, 0))
    subtitle_label.grid(column=0, row=1, columnspan=2, sticky=(tk.W), padx=39, pady=(0, 30))

    # Password input 
    password_entry = tkb.Entry(frame, justify="left", font=main_font, width=35)
    password_entry.grid(row=2, column=0, sticky=(tk.W), padx=40, pady=(0, 5))
    password_entry.configure(takefocus=1)
    password_entry.focus_set()

    def password_check():
        password = password_entry.get()
        check = Password(password)
        score = check.strength()
        meter.configure(amountused=score)

        if score <= 25:
            meter.configure(bootstyle="danger")
        elif score <= 75:
            meter.configure(bootstyle="warning")
        else:
            meter.configure(bootstyle="success")
    
    # Check strength button
    check_strength = tkb.Button(frame, text="Check", width=10, command=password_check, style="Custom.TButton")
    check_strength.grid(column=0, row=3, pady=(5, 0), padx=40, sticky=(tk.W))

    # Strength meter
    meter = tkb.Meter(frame, 
                      metersize=190,
                      subtext="Strength", 
                      interactive=False, 
                      metertype="semi", 
                      stripethickness=10, 
                      bootstyle="",  
                      amountused=0,)
    meter.place(relx=0.815, rely=0.5, anchor=tk.CENTER)

    # Layout
    frame.columnconfigure(1, weight=1)
    check_strength.config(takefocus=0)

    # Binds
    root.bind("<Return>", lambda event: password_check())

    # Event loop
    root.option_add('*focusColor', bg_colour)
    root.configure(bg=bg_colour)
    root.mainloop()








