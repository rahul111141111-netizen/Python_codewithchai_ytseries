input_str = "lsirnoemcwrzpflaqpsi"

for character in input_str:
    print(character)
    if input_str.count(character) == 1:
        print("Your character is", character)
        break
