import json
import math



### PASSWORD CHECK FUNCTIONALITY ###

class Password():
    def __init__(self, password):
        self.password = password
        self.score = 0



    # ### CHECKS ###

    
    # Combined length and diversity check 
    def length_diversity(self):

        password = self.password
        length = len(self.password)

        categories = sum([
            any(c.islower() for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            any(c in '''!@#$%^&*()-_=+{}[];:"\'<>,.?/''' for c in password)
        ])

        if length < 8: 
            return -99
        base = length * 2
        bonus = categories * 10

        return base + bonus


    # Common passwords (WORKING)
    def common_passwords_check(self):
        with open ("data/passwords.json", "r") as file:
            common_passwords = json.load(file)

        common_passwords_lower = {pw.lower() for pw in common_passwords}    # Convert list to lower rather than input (efficiency)

        password_lower = self.password.lower()

        if password_lower in common_passwords_lower:
            return -99
        else:
            return 6
    
    # Personal info (names, movies, etc) (WORKING)
    def common_names_check(self):
        if len (self.password) >= 19:
            return 12
        else:
            with open("data/names.json", "r") as file:
                common_names = json.load(file)
            
            password_lower = self.password.lower()
            
            if any(name.lower() in password_lower for name in common_names):
                return -22
            else:
                return 6

    # Dictionary words (WORKING)
    def dictionary_words_check(self):
        if len (self.password) >= 19:
            return 12
        else:
            with open("data/dictionarywords.json", "r") as file:
                common_words = json.load(file)

            longer_words = [word for word in common_words if len(word) >= 3]
            
            if any(word in self.password for word in longer_words):
                return -22
            else:
                return 6

    # Repeated characters (WORKING)
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
            return -12
        elif any(seq in password_lower for seq in common):
            return -12
        else:
            return 6
        
    # Entropy (randomness)
    def entropy_check(self):
        char_set = set(self.password)
        entropy = len(self.password) * math.log2(len(char_set))

        if entropy < 5:
            return -98
        elif entropy < 25:
            return -60
        elif entropy < 30:
            return 0
        elif entropy < 45:
            return 8
        elif entropy < 65:
            return 14
        else:
            return 23



    ### FINAL STRENGTH ###

    def strength(self):
        self.score = (
            self.length_diversity() +
            self.common_passwords_check() +
            self.common_names_check() +
            self.dictionary_words_check() +
            self.repeat_check() +
            self.entropy_check() 
        )
        if len(self.password) > 20:
            self.score += 10
        return max(1, min(100, self.score))    # 1-100


while True:
    password = input("enter the password: ")

    pwd = Password(password)
    strength = pwd.strength()
    print(f"password score: {strength}")
    print()


