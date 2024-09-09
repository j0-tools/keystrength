class Password():
    def __init__(self, password):
        self.password = password
        self.score = 0

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

    def test_diversity_check():
        test_passwords = [
            "simple",            # only lowercase
            "Simple",            # lowercase + uppercase
            "Simple123",         # lowercase + uppercase + digits
            "Simple123!",        # lowercase + uppercase + digits + special chars
            "123456789",         # only digits
            "ALLUPPERCASE",      # only uppercase
            "Complex#Password9", # well-formed password
            "Password!",         # missing digits
        ]
        
        for pwd in test_passwords:
            p = Password(pwd)
            print(f"Password: {pwd} -> Diversity Score: {p.diversity_check()}")


Password.test_diversity_check()





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
