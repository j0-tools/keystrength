import json

# class Password():
#     def __init__(self, password):
#         self.password = password
#         self.score = 0

#     def diversity_check(self):
    
#         categories = 0
#         score = 0

#         if any(c.islower() for c in self.password):
#             categories += 1
#             score += 4
#         if any(c.isupper() for c in self.password):
#             categories += 1
#             score += 4 
#         if any(c.isdigit() for c in self.password):
#             categories += 1
#             score += 4
#         if any(c in '''!@#$%^&*()-_=+{}[];:"\'<>,.?/''' for c in self.password):
#             categories += 1
#             score += 8

#         if categories == 4:
#             score += 5

#         return score

#     def test_diversity_check():
#         test_passwords = [
#             "simple",            # only lowercase
#             "Simple",            # lowercase + uppercase
#             "Simple123",         # lowercase + uppercase + digits
#             "Simple123!",        # lowercase + uppercase + digits + special chars
#             "123456789",         # only digits
#             "ALLUPPERCASE",      # only uppercase
#             "Complex#Password9", # well-formed password
#             "Password!",         # missing digits
#         ]
        
#         for pwd in test_passwords:
#             p = Password(pwd)
#             print(f"Password: {pwd} -> Diversity Score: {p.diversity_check()}")


# Password.test_diversity_check()

class Password():
    def __init__(self, password):
        self.password = password
        self.score = 0
        
    def dictionary_words_check(self):
        with open("data/dictionarywords.json", "r") as file:
            common_words = json.load(file)
        
        if self.password.lower() in (word.lower() for word in common_words):
            return 0
        else:
            return 15
        

password = "ewgewge"
check = Password(password)
result = check.dictionary_words_check()
print(f"0 if in list // 15 if not in list: {result}")



#     # Length check
#     def length_check(self):
#         length = len(self.password)
#         if length < 8:
#             return 0
#         elif length < 12:
#             return 9
#         elif length < 16:
#             return 14
#         else:
#             return 20
        
# tests = [
#     ("short"),
#     ("mediumpass"),
#     ("longerpassword"),
#     ("verylongpassword12345"),
# ]

# for password in tests:
#     check = Password(password)
#     result = check.length_check()
#     print(f"Password: {password} - Result: {result}")

#print('''!@#$%^&*()-_=+{}[];:"\'<>,.?/''')
