import os
import time
timer = int(input("How long do you want until your device shutdowns (SECONDS):"))
time.sleep(timer)
os.system("shutdown /s /t 1")