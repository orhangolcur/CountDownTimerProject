import time
def countdown(c):
    while c >= 0:
        m, s = divmod(c, 60)
        timer = '{:02d}:{:02d}'.format(m, s)
        print(timer, end="\r")
        time.sleep(1)
        print(c)
        c -= 1
    print('Fire in the hole!!')

c = input("Enter the time value in seconds: ")

print("The countdown timer has started....")

countdown(int(c))