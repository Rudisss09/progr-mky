import datetime
import time

currentTime = datetime.datetime.now().strftime("%H:%M")
alarmTime = input("zadej nejaky ten čas (format: hh:mm): ")

while True:
    currentTime = datetime.datetime.now().strftime("%H:%M")

    if currentTime == alarmTime:
        print("budíček")
        time.sleep(60)

    time.sleep(1)