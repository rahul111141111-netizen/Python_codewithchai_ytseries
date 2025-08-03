distance = 23

if distance < 3:
    Transport = "walk"
elif distance < 10:
    Transport = "bike"

else:
    Transport = "car"

print("Suggested mode of transport:", Transport)
# The code suggests a mode of transport based on the distance.