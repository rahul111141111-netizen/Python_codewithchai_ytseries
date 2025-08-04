numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0

for x in numbers:
    if x > 0:
        positive_number_count += 1
        # positive_number_count = positive_number_count + 1:
print("Final count of positive numbers in list is",  str(positive_number_count) + ".")

