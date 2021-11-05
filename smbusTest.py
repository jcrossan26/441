import smbus
mybus = smbus.SMBus(1)

value = mybus.read_byte(0x48)
while(1==1):
  print(value)