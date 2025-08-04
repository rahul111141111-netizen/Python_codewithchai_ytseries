number = int(input("what will it be: ") )
for i in range(1,11):
    if i == 5:
        continue
    print(number, "x", i, "=", i * number)  
    