import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO_PIR=7
GPIO.setup(GPIO_PIR, GPIO.IN)
needs_answer=false
question = 0
while True:
    if GPIO.input(GPIO_PIR) == 1:
        if needs_answer and question == 1:
            os.system("espeak -ven+f3 -k5 -s150 \"Matter is anyting that has a mass and takes up space\"")
        if needs_answer and question == 2:
            os.system("espeak -ven+f3 -k5 -s150 \"There are seven days in a week\"")
        if needs_answer and question == 3:
            os.system("espeak -ven+f3 -k5 -s150 \"Erwin Schrodinger created the famous thought experiment involving a cat\"")
        if needs_answer and question == 4:
            os.system("espeak -ven+f3 -k5 -s150 \"E equals m c squared is Einstein's most famous equation\"")
        if needs_answer and question == 5:
            os.system("espeak -ven+f3 -k5 -s150 \"The United States is part of the continent of North America\"")
        if needs_answer and question == 6:
            os.system("espeak -ven+f3 -k5 -s150 \"Zero Kelvin is equal to negative two hundred seventy-three and fifteen-hundredths degrees celsius\"")
        if needs_answer and question == 7:
            os.system("espeak -ven+f3 -k5 -s150 \"A spider has eight legs\"")
        if needs_answer and question == 8:
            os.system("espeak -ven+fe -k5 -s150 \"America fought Great Britain in the American Revolution\"")
        if needs_answer and question == 9:
            os.system("espeak -ven+f3 -k5 -s150 \"There are twenty-six letters in the English alphabet\"")
        if needs_answer and question == 10:
            os.system("espeak -ven+f3 -k5 -s150 \"The five senses are taste, touch, hearing, sight, and scent\"")
    
            #
            #
            #
        else:
            question = random.randint(1,11)
            if question == 1:
                os.system("espeak -ven+f3 -k5 -s150 \"What is matter\"")
            if question == 2:
                os.system("espeak -ven+f3 -k5 -s150 \"How many days are in a week\"")
            if question == 3:
                os.system("espeak -ven+f3 -k5 -s150 \"Who created the famous thought experiment involving a cat\"")
            if question == 4:
                os.system("espeak -ven+f3 -k5 -s150 \"What is Einstein's most famous equation\"")
            if question == 5:
                os.system("espeak -ven+f3 -k5 -s150 \"What continent is the United States a part of\"")
            if question == 6:
                os.system("espeak -ven+f3 -k5 -s150 \"What is zero degrees kelvin equal to in celsius\"")
            if question == 7:
                os.system("espeak -ven+f3 -k5 -s150 \"How many legs does a spider have\"")
            if question == 8:
                os.system("espeak -ven+f3 -k5 -s150 \"Who did America fight in the American Revolution\"")
            if question == 9:
                os.system("espeak -ven+f3 -k5 -s150 \"How many letters are in the English alphabet\"")
            if question == 10:
                os.system("espeak -ven+f3 -k5 -s150 \"What are the five senses\"")
            time.sleep(5)
