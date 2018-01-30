import micropython
from machine import I2C, Pin, Timer
from lis2hh12 import LIS2HH12, FS_2G, ODR_OFF, ODR_50HZ
from fusion import Fusion

micropython.alloc_emergency_exception_buf(100)

i2c = I2C(scl=Pin(26), sda=Pin(25))
sensor = LIS2HH12(i2c, fs=FS_2G, odr=ODR_50HZ)
imu = Fusion()

def update_imu(timer):
    imu.update_nomag(sensor.read(), (0,0,0))

def read_imu(timer):
    imu.update_nomag(sensor.read(), (0,0,0))
    print("{:7.3f} {:7.3f} {:7.3f}".format(imu.heading, imu.pitch, imu.roll))


timer_0 = Timer(0)
timer_0.init(period=100, mode=Timer.PERIODIC, callback=update_imu)

timer_1 = Timer(1)
timer_1.init(period=1000, mode=Timer.PERIODIC, callback=read_imu)
