#imports
from win10toast import ToastNotifier
import time #for timer

toaster=ToastNotifier()
title = input("\nEnter the title of the reminder: ")
msg = input("\nEnter the message of the reminder: ")
min=float(input("\nEnter the time in minutes: "))
sec=min*60
print("\nReminder set for "+str(min)+" minutes")
time.sleep(sec)
toaster.show_toast(title,msg,duration=10,threaded=True)
while toaster.notification_active():
    time.sleep(0.1)