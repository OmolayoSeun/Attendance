from datetime import datetime

txt = datetime.now().strftime("%H:%M:%S")

timeList = txt.split(":")
hour = int(timeList[0])
minutes = int (timeList[1])

if hour > 8 or (hour == 8 and minutes > 30):
    print("you came late")
print(hour)
print(minutes)
