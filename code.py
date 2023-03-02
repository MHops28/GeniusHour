sudo apt-get install espeak


Import RPi.GPIO as GPIO
Import time
import os
GPIO.setmode(GPIO.BCM)
GPIO_PIR=7
GPIO.setup(GPIO_PIR, GPIO.IN)

Current_State= 0
Previous_State= 0

Try:
While GPIO.input(GPIO_PIR)==1:
Current_State= 0
If Current_State=1 and Previous_State=0:
question = random.randint(1,10)
If question== 1:
	os.system(“espeak -ven+f3 -k5 -s150 \“What is matter\””)
	#Insert Email mechanism here
	While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “Matter is anything that has a mass and takes up space”
If question==2:
espeak -ven+f3 -k5 -s150 “How many days are in a week”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “There are seven days in a week”
If question== 3:
	espeak -ven+f3 -k5 -s150 “What is Einstein’s most famous equation?”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “Einstein’s most famous equation is E equals m c squared”
If question==4:
	espeak -ven+f3 -k5 -s150 “Who created the famous thought experiment involving a cat?”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “Erwin Schrodinger created the famous thought experiment involving a cat”
If question==5:
	espeak -ven+f3 -k5 -s150 “What continent is the united states part of”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “The United States is part of the continent of North America”
If question==6:
	espeak -ven+f3 -k5 -s150 “What is zero kelvin equal to in celsius and fahrenheit”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “Zero kelvin is equal to negative two hundred seventy-three and fifteen-hundredths degrees celsius and negative four hundred fifty-nine and sixty-seven hundredths degrees fahrenheit”
If question==7:
espeak -ven+f3 -k5 -s150 “How many legs does a spider have”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “A spider has eight legs”
If question==8:
	espeak -ven+f3 -k5 -s150 “Who did America fight against in the American Revolution”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “America fought against Great Britain in the American Revolution”
If question==9
	espeak -ven+f3 -k5 -s150 “How many letters are there in the English alphabet”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “There are twenty-six letters in the English alphabet”
If question ==10
	espeak -ven+f3 -k5 -s150 “What are the five senses”
While GPIO.input(GPIO_PIR)== 0:
	Espeak -ven+f3 -k5 -s150 “The five senses are touch, taste, hearing, sight, and smell”
