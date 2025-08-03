passsword = "sdf desed"
Password_lengh = len(passsword) 
if Password_lengh < 6:
    passsword_strength = "weak"
elif  Password_lengh <= 10:
    passsword_strength = "medium"
else:
    passsword_strength = "strong"
print("Password strength:", passsword_strength)
# The code checks the strength of a password based on its length.