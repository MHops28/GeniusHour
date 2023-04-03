import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO_PIR=7
GPIO.setup(GPIO_PIR, GPIO.IN)

while True:
    if GPIO.input(GPIO_PIR) == 1:
        question = 1
        if question == 1:
            os.system("espeak -ven+f3 -k5 -s150 \"What is matter\"")
        # if question == 2:
        #     os.system("espeak -ven+f3 -k5 -s150 \"How many days are in a week\"")
        
        #
        #
        #
        #