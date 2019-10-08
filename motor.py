import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from time import sleep

Motor1A = 5 
Motor1B = 6
Motor2A = 19
Motor2B = 13
en1 = 1

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

p1=GPIO.PWM(en1,100)
p1.start(25)

GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.LOW)

def forward():
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

def backward():
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

def turnRight():
	print("Going Right")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

def turnLeft():
	print("Going Left")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

def stop():
	print("Stopping")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)

def low():
	print("Low")
	p1.ChangeDutyCycle(25)
	
def medium():
	print("medium")
        p1.ChangeDutyCycle(50)

def high():
	print("high")
        p1.ChangeDutyCycle(75)

while(1):

    	x=raw_input()

	if x=='r':
		forward()
		x='z'
	elif x=='s':
		stop()
		x='z'
	elif x=='f':
		forward()
		x='z'
	elif x=='b':
		backward()
		x='z'
	elif x=='l':
		low()
		x='z'
	elif x=='m':
		medium()
		x='z'
	elif x=='h':
		high()
		x='z'
	elif x=='a':
		turnLeft()
		x='z'
	elif x=='d':
		turnRight()
		x='z'
	elif x=='e':
		GPIO.cleanup()
		print("GPIO Clean up")
		break
	else:
        	print("<<<  wrong data  >>>")
	     	print("please enter the defined data to continue.....")