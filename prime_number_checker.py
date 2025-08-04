number = 13

Is_prime_number = True

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            Is_prime_number = False
            break

if Is_prime_number == True:
    print(number,"is prime number")
else:
    print(number,"is NOT a prime number")


