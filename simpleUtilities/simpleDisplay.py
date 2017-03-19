from machine import Pin, I2C

i2c = I2C(scl=Pin(16), sda=Pin(5), freq=100000)
i2c.readfrom(0x3a, 5)
i2c.writeto(0x3a, '12')
buf = bytearray(10) 
i2c.writeto(0x3a, buf)

