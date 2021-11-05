import smbus
mybus = smbus.SMBus(1)

value = mybus.read_byte(01001000)
while(1==1):
  print(value)