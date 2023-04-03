#sudo apt-get install espeak


import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO_PIR=7
GPIO.setup(GPIO_PIR, GPIO.IN)

Current_State= 0
Previous_State= 0

try:
    while GPIO.input(GPIO_PIR)==1:
        if Current_State==1 and Previous_State==0:
            question = random.randint(1,10)
        if question== 1:
	        os.system("espeak -ven+f3 -k5 -s150 \"What is matter\"")
	#Insert Email mechanism here
	while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 \“Matter is anything that has a mass and takes up space\”")
        if question==2:
            os.system("espeak -ven+f3 -k5 -s150 \“How many days are in a week\”")
    while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 \“There are seven days in a week\”")
        if question== 3:
	        os.system("espeak -ven+f3 -k5 -s150 \“What is Einstein’s most famous equation?\”")
    while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 \“Einstein’s most famous equation is E equals m c squared\”")
        if question==4:
	        os.system("espeak -ven+f3 -k5 -s150 \“Who created the famous thought experiment involving a cat?\”")
    while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 \“Erwin Schrodinger created the famous thought experiment involving a cat\”")
        if question==5:
	        os.system("espeak -ven+f3 -k5 -s150 \“What continent is the united states part of\”")
    while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 \“The United States is part of the continent of North America\”")
        if question==6:
	        os.system("espeak -ven+f3 -k5 -s150 \“What is zero kelvin equal to in celsius and fahrenheit\”")
    while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 /“Zero kelvin is equal to negative two hundred seventy-three and fifteen-hundredths degrees celsius and negative four hundred fifty-nine and sixty-seven hundredths degrees fahrenheit/”")
        if question==7:
            os.system("espeak -ven+f3 -k5 -s150 /“How many legs does a spider have/”")
    while GPIO.input(GPIO_PIR)== 0:
            os.system("espeak -ven+f3 -k5 -s150 /“A spider has eight legs/”")
        if question==8:
	        os.system("espeak -ven+f3 -k5 -s150 /“Who did America fight against in the American Revolution/”")
    while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 \“America fought against Great Britain in the American Revolution\”")
        if question==9
	        os.system("espeak -ven+f3 -k5 -s150 /“How many letters are there in the English alphabet/”")
    while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 \“There are twenty-six letters in the English alphabet\”")
        if question ==10
	        os.system("espeak -ven+f3 -k5 -s150 /“What are the five senses/”")
    while GPIO.input(GPIO_PIR)== 0:
	        os.system("espeak -ven+f3 -k5 -s150 /“The five senses are touch, taste, hearing, sight, and smell/"")
Except: 
    Current_State= 0 and Current_State= 0
    