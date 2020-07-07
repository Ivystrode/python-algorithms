import datetime
import time

reminder = True
while reminder == True:
    if datetime.datetime.now().strftime('%H%M') == '1851':
        print("yes its time")
        reminder = False
    else:
        print("not yet")
    time.sleep(5)