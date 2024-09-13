import json
import math



### PASSWORD CHECK FUNCTIONALITY ###

class Password():
    def __init__(self, password):
        self.password = password
        self.score = 0



    ### CHECKS ###

    # Length check (WORKING)
    def length_check(self):
        length = len(self.password)
        if length < 9:
            return -13
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
    
    # Diversity check (WORKING)
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

        score = categories * 4
        
        if categories == 4:
            score += 10

        if categories <= 1:
            score -= 10

        return score
    
    # Common passwords (WORKING)
    def common_passwords_check(self):
        if len (self.password) >= 25:
            return 5
        if len (self.password) >= 20:
            return 3
        else:
            with open ("data/passwords.json", "r") as file:
                common_passwords = json.load(file)

            password_lower = self.password.lower()

            if password_lower in (pw.lower() for pw in common_passwords):
                return -33
            else:
                return 8
    
    # Personal info (names, movies, etc) (WORKING)
    def common_names_check(self):
        if len (self.password) >= 15:
            return 5
        else:
            with open("data/names.json", "r") as file:
                common_names = json.load(file)
            
            password_lower = self.password.lower()
            
            if any(name.lower() in password_lower for name in common_names):
                return -5
            else:
                return 8

    # Dictionary words (WORKING)
    def dictionary_words_check(self):
        if len (self.password) >= 15:
            return 5
        else:
            with open("data/dictionarywords.json", "r") as file:
                common_words = json.load(file)

            longer_words = [word for word in common_words if len(word) >= 3]
            
            if any(word in self.password for word in longer_words):
                return -5
            else:
                return 8

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
        elif entropy < 35:
            return -10
        elif entropy < 40:
            return 5
        elif entropy < 55:
            return 10
        elif entropy < 75:
            return 15
        else:
            return 20



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


while True:
    password = input("enter the password: ")

    pwd = Password(password)
    strength = pwd.strength()
    print(f"password score: {strength}")
    print()


