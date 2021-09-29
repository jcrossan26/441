import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#Input GPIO for buttons
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

#Output GPIO for LEDs
GPIO.setup(16, GPIO.OUT, initial=0)
GPIO.setup(20, GPIO.OUT, initial=0)
GPIO.setup(21, GPIO.OUT, initial=0)

button1 = GPIO.input(23)
button2 = GPIO.input(24)

pwm1 = GPIO.PWM(16,1)

def callback1():
  GPIO.output(16,1)
  print("Detected")

while True:
  GPIO.add_event_detect(
    23,
    GPIO.RISING,
    callback=callback1,
    bouncetime=100
  )


  GPIO.remove_event_detect(23)