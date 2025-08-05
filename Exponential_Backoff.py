import time

wait_time = 1
retries_limit = 5
attempt = 0


while attempt < retries_limit:
    print("Attempt number", attempt +1, "wait time -", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1


password = "dawg"

user_input_password = input("")
while True:
    user_input_password == input("dawg")

    if attempt < retries_limit:
        if  user_input_password == dawg:
            print("Access Granted!")
            break
    else:
        print("access denied")
        print("attempts made", attempt, "wait for ", wait_time, "attempts left", retries_limit-1)
        time.sleep(wait_time)
        attempt += 1
        wait_time *= 2
else:
    print("BLOCKED") 