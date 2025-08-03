activity = {"sunny": "go for a walk",
            "rainy": "stay indoors and read a book",
            "snowy": "build a snowman",}
weather = input("Enter the weather condition, ").lower()
suggested_activity = activity.get(weather, "do cool shits")
print("Suggested activity:", suggested_activity)
