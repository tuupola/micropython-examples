import gc
import micropython
from machine import I2C, Pin, Timer
from gnssl76l import GNSSL76L
from micropyGPS import MicropyGPS

micropython.alloc_emergency_exception_buf(100)

i2c = I2C(scl=Pin(26), sda=Pin(25))
receiver = GNSSL76L(i2c)
gps = MicropyGPS()

def read_receiver(timer):
    for sentence in receiver.sentences():
        # MicropyGPS wants data char by char.
        # This is quite inefficient.
        for char in sentence:
            gps.update(chr(char))

    print(gps.latitude)
    print(gps.longitude)
    print(gps.speed)
    print(gc.mem_free())

timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=read_receiver)

