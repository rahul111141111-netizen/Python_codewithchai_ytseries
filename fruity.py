fruit_color = {"yellow": "ripe", "green" : "unripe", "brown": "overripe"}
color = input("Enter the color of the fruit: ")

fruit_status = print("fruit is", fruit_color.get(color, "unknown color"))