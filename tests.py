import json
import math



### PASSWORD CHECK FUNCTIONALITY ###

class Password():
    def __init__(self, password):
        self.password = password
        self.score = 100



    # ### CHECKS ###

    # # Length check (WORKING)
    # def length_check(self):
    #     length = len(self.password)
    #     if length < 8:
    #         return -30
    #     elif length < 11:
    #         return 0
    #     elif length < 13:
    #         return 4
    #     elif length < 18:
    #         return 8
    #     else:
    #         return 34
    
    # # Diversity check (WORKING)
    # def diversity_check(self):

    #     if len (self.password) >= 18:
    #         return 11

    #     else:
    #         categories = 0
    #         score = 0

    #         if any(c.islower() for c in self.password):
    #             categories += 1
    #         if any(c.isupper() for c in self.password):
    #             categories += 1
    #         if any(c.isdigit() for c in self.password):
    #             categories += 1
    #         if any(c in '''!@#$%^&*()-_=+{}[];:"\'<>,.?/''' for c in self.password):
    #             categories += 1

    #         score = categories * 3
            
    #         if categories == 4:
    #             score += 10

    #         if categories < 4 and len(self.password) < 15:
    #             score -= 11 

    #         if categories <= 1:
    #             score -= 15

    #         return score
    

    # Combined length and diversity check 
    def length_diversity(self):
        length = len(self.password)

        if length < 8:
            return -99

        categories = 0

        has_lower = any(c.islower() for c in self.password)
        has_upper = any(c.isupper() for c in self.password)
        has_digits = any(c.isdigit() for c in self.password)
        has_symbols = any(c in '''!@#$%^&*()-_=+{}[];:"\'<>,.?/''' for c in self.password)

        if has_digits and not (has_lower or has_upper or has_symbols):    # Numbers only
            pass

        elif has_lower and not (has_upper or has_digits or has_symbols):    # Lowercase only 
            pass

        elif has_upper and not (has_lower or has_digits or has_symbols):    # Uppercase only 
            pass

        elif has_digits and has_symbols and not (has_lower or has_upper):    # Digits and symbols
            pass

        elif has_lower and has_symbols and not (has_upper or has_digits):    # Lowercase and symbols
            pass

        elif has_upper and has_symbols and not (has_lower or has_digits):    # Upper and symbols
            pass

        elif has_lower and has_upper and not (has_digits or has_symbols):    # Upper and lowercase
            pass

        elif has_lower and has_upper and has_symbols and not has_digits:    # Lower, upper and symbols
            pass

        elif has_lower and has_digits and has_symbols and not has_upper:    # Lower, digit and symbol
            pass

        elif has_upper and has_digits and has_symbols and not has_lower:    # Upper, digit and symbol
            pass

        elif has_digits and has_lower and has_upper and not has_symbols:    # Digit, upper, and lower
            pass

        elif has_digits and has_lower and has_upper and has_symbols:    # All
            pass



            
        
            


    # # Common passwords (WORKING)
    # def common_passwords_check(self):
    #     with open ("data/passwords.json", "r") as file:
    #         common_passwords = json.load(file)

    #     common_passwords_lower = {pw.lower() for pw in common_passwords}    # Convert list to lower rather than input (efficiency)

    #     password_lower = self.password.lower()

    #     if password_lower in common_passwords_lower:
    #         return -100
    #     else:
    #         return 6
    
    # # Personal info (names, movies, etc) (WORKING)
    # def common_names_check(self):
    #     if len (self.password) >= 18:
    #         return 11
    #     else:
    #         with open("data/names.json", "r") as file:
    #             common_names = json.load(file)
            
    #         password_lower = self.password.lower()
            
    #         if any(name.lower() in password_lower for name in common_names):
    #             return -8
    #         else:
    #             return 6

    # # Dictionary words (WORKING)
    # def dictionary_words_check(self):
    #     if len (self.password) >= 18:
    #         return 11
    #     else:
    #         with open("data/dictionarywords.json", "r") as file:
    #             common_words = json.load(file)

    #         longer_words = [word for word in common_words if len(word) >= 3]
            
    #         if any(word in self.password for word in longer_words):
    #             return -6
    #         else:
    #             return 6

    # # Repeated characters (WORKING)
    # def repeat_check(self):
        
    #     password_lower = self.password.lower()
    #     common = [
    #     # Alphabetic
    #     "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij",
    #     "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr",
    #     "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz",
    #     # Reverse
    #     "zyx", "yxw", "xwv", "wvu", "vut", "uts",
    #     # Numeric
    #     "123", "234", "345", "456", "567", "678", "789", "890",
    #     # Reverse numeric
    #     "987", "876", "765", "654", "543", "432", "321",
    #     # Keyboard patterns
    #     "qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop",
    #     "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl",
    #     "zxc", "xcv", "cvb", "vbn", "bnm",
    #     # Keyboard patterns (AZERTY)
    #     "aze", "zer", "ert", "rty", "tyu", "yui", "uio", "iop",
    #     "qsd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "lm",
    #     "wxc", "xcv", "cvb", "vbn",
    #     # Common substitutions
    #     "!@#", "@#$", "#$%", "$%^", "%^&", "^&*", "&*(", "*()"]

    #     if any(password_lower.count(c) > 2 for c in set(password_lower)):
    #         return -8
    #     elif any(seq in password_lower for seq in common):
    #         return -8
    #     else:
    #         return 11
        
    # # Entropy (randomness)
    # def entropy_check(self):
    #     char_set = set(self.password)
    #     entropy = len(self.password) * math.log2(len(char_set))

    #     if entropy < 5:
    #         return -50
    #     elif entropy < 25:
    #         return -10
    #     elif entropy < 30:
    #         return 0
    #     elif entropy < 45:
    #         return 5
    #     elif entropy < 65:
    #         return 10
    #     else:
    #         return 20



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
        if len(self.password) > 30:
            self.score += 5
        return max(1, min(100, self.score))    # 1-100


while True:
    password = input("enter the password: ")

    pwd = Password(password)
    strength = pwd.strength()
    print(f"password score: {strength}")
    print()


