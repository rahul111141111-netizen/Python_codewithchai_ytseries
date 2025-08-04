items = ["apple", "banana", "orange", "apple", "mango"]

unique_items =set()
for item in items:
    if item in unique_items:
        print("duplicate is", item)
        break
    unique_items.add(item) 
 
 #Okay, so I think I got the point. Initially, when the code is run, 
 # it is run while the initial unique items set is empty at that time. 
 # So, the second it sees something again in it, it will find that as duplicate. 
 # So, that's why this code is working right.