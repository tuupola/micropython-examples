#
# This file is part of MicroPython examples
# Copyright (c) 2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-examples
#

# pylint: disable=import-error
import micropython
import m5stack
from machine import I2C, Pin, Timer
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_DEG_S
from fusion import Fusion
# pylint: enable=import-error

micropython.alloc_emergency_exception_buf(100)

tft = m5stack.Display()
tft.font(tft.FONT_Default)

tft.text(60, 90, "HEADING:")
tft.text(88, 110, "PITCH:")
tft.text(102, 130, "ROLL:")

i2c = I2C(scl=Pin(22), sda=Pin(21))
mpu6500 = MPU6500(i2c, gyro_sf=SF_DEG_S) # Fusion expects deg/s
sensor = MPU9250(i2c, mpu6500=mpu6500)
imu = Fusion()

def update_imu(timer):
    imu.update(sensor.acceleration, sensor.gyro, sensor.magnetic)

def display_imu(timer):
    tft.text(180, 90, "{:3.1f}\r".format(imu.heading))
    tft.text(180, 110, "{:3.1f}\r".format(imu.pitch))
    tft.text(180, 130, "{:3.1f}\r".format(imu.roll))

timer_0 = Timer(0)
timer_0.init(period=100, mode=Timer.PERIODIC, callback=update_imu)

timer_1 = Timer(1)
timer_1.init(period=500, mode=Timer.PERIODIC, callback=display_imu)
