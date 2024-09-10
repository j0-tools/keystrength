import json



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
    
    # Common passwords (WORKING)
    def common_passwords_check(self):
        with open ("data/passwords.json", "r") as file:
            common_passwords = json.load(file)

        password_lower = self.password.lower()

        if any(word.lower() in password_lower for word in common_passwords):
            return 0
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
            return 15

    # Dictionary words (WORKING)
    def dictionary_words_check(self):
        with open("data/dictionarywords.json", "r") as file:
            common_words = json.load(file)

        password_lower = self.password.lower()
        
        if any(word.lower() in password_lower for word in common_words):
            return 0
        else:
            return 15

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
            return 3
        else:
            return 5



    ### FINAL STRENGTH ###

    # Strength
    def strength(self):
        self.score += self.length_check()
        self.score += self.diversity_check()
        self.score += self.common_passwords_check()
        self.score += self.common_names_check()
        self.score += self.dictionary_words_check()
        self.score += self.repeat_check()
        self.score += self.entropy_check()
        return self.score


while True:
    password = input("enter the password: ")
