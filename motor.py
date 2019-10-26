import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Define GPIO pins for motors
"""
LB = Left Backward
LF = Left Forward
RB = Right Backward
RF = Right Forward
enL = Control Left motor speed
enR = Control Right motor speed
"""
MotorLB = 19
MotorLF = 13
MotorRB = 5
MotorRF = 6
enL = 7
enR = 1

GPIO.setwarnings(False)
GPIO.setup(MotorLF, GPIO.OUT)
GPIO.setup(MotorLB, GPIO.OUT)
GPIO.setup(MotorRF, GPIO.OUT)
GPIO.setup(MotorRB, GPIO.OUT)
#Set frequency for 2 control speed pins
pL = GPIO.PWM(enL, 1000)
pR = GPIO.PWM(enR, 1000)

#Set speed at the beginning
a = 15
pL.start(a)
pR.start(a)

#Set 2 motors to stop at the beginning
GPIO.output(MotorLF, GPIO.LOW)
GPIO.output(MotorLB, GPIO.LOW)
GPIO.output(MotorRF, GPIO.LOW)
GPIO.output(MotorRB, GPIO.LOW)

#Reset both motors speed to the same value
def reset(b):
	pL.ChangeDutyCycle(b)
	pR.ChangeDutyCycle(b)

#Stop motor
def stop():
	GPIO.output(MotorLF, GPIO.LOW)
	GPIO.output(MotorLB, GPIO.LOW)
	GPIO.output(MotorRF, GPIO.LOW)
	GPIO.output(MotorRB, GPIO.LOW)

#Clean GPIO set up
def clean():
	GPIO.cleanup()
"""Control motors direction"""

def backward():
	GPIO.output(MotorLB, GPIO.HIGH)
	GPIO.output(MotorLF, GPIO.LOW)
	GPIO.output(MotorRB, GPIO.HIGH)
	GPIO.output(MotorRF, GPIO.LOW)
	reset(a)

def forward():
	GPIO.output(MotorLB, GPIO.LOW)
	GPIO.output(MotorLF, GPIO.HIGH)
	GPIO.output(MotorRB, GPIO.LOW)
	GPIO.output(MotorRF, GPIO.HIGH)
	reset(a)

def right():
	reset(5)
	pL.ChangeDutyCycle(25)
	pR.ChangeDutyCycle(10)

def left():
	reset(5)
	pL.ChangeDutyCycle(5)
	pR.ChangeDutyCycle(35)