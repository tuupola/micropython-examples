## Heading, Pitch and Roll With MPU-9250

Read an I2C 9DOF sensor using an timer. Prints out heading, pitch and roll on M5Stack TFT display. Uses [MPU-9250 I2C driver](https://github.com/tuupola/micropython-mpu9250) and [sensor fusion](https://github.com/micropython-IMU/micropython-fusion) for heading,  pitch and roll calculations.

If your board seems to be unresponsive open REPL, copy paste the following and reboot.

```python
import os
os.remove("main.py")
```