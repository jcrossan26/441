import RPi.GPIO as GPIO
import time
import smbus
mybus = smbus.SMBus(1)

GPIO.setmode(GPIO.BCM)
pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)


class zero():
  lightValueOld = 100
  # Make a full rotation of the output shaft:
  def loop(dir): # dir = rotation direction (cw or ccw)
    for i in range(512): # full revolution (8 cycles/rotation * 64 gear ratio)
      zeroStep = i
      for halfstep in range(8): # 8 half-steps per cycle
        for pin in range(4):    # 4 pins that need to be energized
          GPIO.output(pins[pin], dir[halfstep][pin])
        lightValueNew = mybus.read_byte(0x48)
        if(lightValueNew < lightValueOld):
          return(zeroStep)
          break

        delay_us(3000)
try:
  loop(cw)
GPIO.cleanup() 


zeroAngle = zero()
print(zeroAngle)
