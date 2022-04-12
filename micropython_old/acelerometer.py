import mpu6050
from pyb import I2C, Pin

i2c = I2C(1)
acc = mpu6050.accel(i2c) #实例化accel类

acc.get_values()    #调用方法，返回一次全部数值