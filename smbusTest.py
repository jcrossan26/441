import smbus
mybus = smbus.SMBus(1)

while(1==1):
  value = mybus.read_byte(0x48)
  print(value)