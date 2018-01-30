## Quectel GNSS L76-L and MicropyGPS

Uses [Quectel GNSS L76-L I2C](https://github.com/tuupola/micropython-gnssl76l) driver and [micropyGPS](https://github.com/inmcm/micropyGPS).

Feeding NMEA sentences character by character is a quite unefficient. If your board seems to be unresponsi ve open REPL, copy paste the following and reboot.

```python
import os
os.remove("main.py")
```