## Pitch and Roll With LIS2HH12 Accelerometer

Uses [LIS2HH12 I2C driver](https://github.com/tuupola/micropython-lis2hh12) and [sensor fusion](https://github.com/micropython-IMU/micropython-fusion).

If your board seems to be unresponsive open REPL, copy paste the following and reboot.

```python
import os
os.remove("main.py")
```