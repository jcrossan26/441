import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#Input GPIO for buttons
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Output GPIO for LEDs
GPIO.setup(16, GPIO.OUT, initial=0)
GPIO.setup(20, GPIO.OUT, initial=0)
GPIO.setup(21, GPIO.OUT, initial=0)

button1 = GPIO.input(23)
button2 = GPIO.input(24)

pwm1 = GPIO.PWM(16,1)

def callback1(23):
  GPIO.output(16,1)

while True:
  GPIO.add_event_detect(
    23,
    GPIO.FALLING,
    callback=callback1,
    bouncetime=100
  )


  GPIO.remove_event_detect(23)