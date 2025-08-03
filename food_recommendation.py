
pet = "dog"
age = 2
pet_species = ("cat", "dog")

if pet == (pet_species)[0] and age >=5: 
    print("senior cat food")
elif pet == (pet_species)[0] and age < 5:
    print("junior cat food")

if pet == (pet_species)[1] and age <= 2:
    print("puppy food")
elif pet == (pet_species)[1] and age > 2:
    print("big dawg food")

#LOWER ONE IS FROM GPT MORE CLEAN
pet = input("Enter Pet Type: ").lower()
age = int(input("Enter Pet Age: "))

if pet == "dog":
    if age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")
elif pet == "cat":
    if age >= 5:
        print("Senior cat food")
    else:
        print("Junior cat food")
else:
    print("Sorry, we don't have food for this pet.")


#gemini clean code
pet = "dog"
age = 2

# Check for cat first
if pet == "cat":
    if age >= 5:
        print("senior cat food")
    else:
        print("junior cat food")

# Then check for dog
elif pet == "dog":
    if age <= 2:
        print("puppy food")
    else:
        print("big dawg food")

# Optional: Handle other pets
else:
    print("Sorry, we only have food for cats and dogs.")
