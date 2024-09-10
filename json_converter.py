import json

# Common passwords
with open("data/passwords.txt", "r") as file:
    lines = file.readlines()

passwords = [line.split()[0] for line in lines if line.strip()]

json_data = json.dumps(passwords, indent=4)

with open("data/passwords.json", "w") as file:
    file.write(json_data)