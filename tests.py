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
        if length < 8:
            return -5
        elif length < 12:
            return 5
        elif length < 16:
            return 15
        else:
            return 30
    
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

        score = categories * 3
        if categories == 4:
            score += 7

        return score
    
    # Common passwords (WORKING)
    def common_passwords_check(self):
        with open ("data/passwords.json", "r") as file:
            common_passwords = json.load(file)

        password_lower = self.password.lower()

        if any(word.lower() in password_lower for word in common_passwords):
            return -10
        else:
            return 15
    
    # Personal info (names, movies, etc) (WORKING)
    def common_names_check(self):
        with open("data/names.json", "r") as file:
            common_names = json.load(file)
        
        password_lower = self.password.lower()
        
        if any(name.lower() in password_lower for name in common_names):
            return 0
        else:
            return 5

    # Dictionary words (WORKING)
    def dictionary_words_check(self):
        with open("data/dictionarywords.json", "r") as file:
            common_words = json.load(file)

        longer_words = [word for word in common_words if len(word) >= 3]
        
        if any(word in self.password for word in longer_words):
            return 0
        else:
            return 5

    # Repeated characters (WORKING)
    def repeat_check(self):
        if any(self.password.count(c) > 3 for c in set(self.password)) or "abc" in self.password or "123" in self.password:
            return 0
        else:
            return 10
        
    # Entropy (randomness) (AI MADE THIS FUNCTION - TEST)
    def entropy_check(self):
        char_set = set(self.password)
        entropy = len(self.password) * math.log2(len(char_set))

        if entropy < 40:
            return 0
        elif entropy < 60:
            return 5
        elif entropy < 80:
            return 10
        else:
            return 20



    ### FINAL STRENGTH ###

    # Strength
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
        return max(0, min(100, self.score))    # 0-100


while True:
    password = input("enter the password: ")

    pwd = Password(password)
    strength = pwd.strength()
    print(f"password score: {strength}")
    print()


