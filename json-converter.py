import json


# # Common passwords
# with open("data/passwords.txt", "r") as file:
#     lines = file.readlines()

# passwords = [line.split()[0] for line in lines if line.strip()]

# json_data = json.dumps(passwords, indent=4)

# with open("data/passwords.json", "w") as file:
#     file.write(json_data)


# # Common names/surnames
# with open("data/names.txt", "r") as file:
#     lines = file.readlines()

# names = [line.strip() for line in lines if line.strip()]

# json_data = json.dumps(names, indent=4)

# with open("data/names.json", "w") as file:
#     file.write(json_data)


# Dictionary words
with open("data/dictionarywords.txt", "r") as file:
    lines = file.readlines()

words = [line.split()[0] for line in lines if line.strip()]

json_data = json.dumps(words, indent=4)

with open("data/dictionarywords.json", "w") as file:
    file.write(json_data)
