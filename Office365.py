import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Good work.")

if __name__ == "__main__":
    focus_time = int(input("How many minutes do you want to focus for? "))
    focus_timer(focus_time)
