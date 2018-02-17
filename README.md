# MicroPython experiments

## Heading, Pitch and Roll With MPU-9250

Read an I2C 9DOF sensor using an timer. Prints out heading, pitch and roll on TFT display. Uses [MPU-9250 I2C driver](https://github.com/tuupola/micropython-mpu9250) and [sensor fusion](https://github.com/micropython-IMU/micropython-fusion) for heading,  pitch and roll calculations.

## Quectel GNSS L76-L and MicropyGPS

Reads an I2C GPS receiver using an timer. Prints out current coordinates and speed. Uses [Quectel GNSS L76-L I2C](https://github.com/tuupola/micropython-gnssl76l) and [micropyGPS](https://github.com/inmcm/micropyGPS) for parsin NMEA sentences.

## Pitch and Roll With LIS2HH12 Accelerometer

Read an I2C accelerometer using an timer. Prints out pitch and roll. Uses [LIS2HH12 I2C driver](https://github.com/tuupola/micropython-lis2hh12) and [sensor fusion](https://github.com/micropython-IMU/micropython-fusion) for pitch and roll calculations.

## Geolocation Without GPS

Scans the nearby wifi networks and locates the board using [Google Maps Geolocation API](https://developers.google.com/maps/documentation/geolocation/intro). After locating script downloads and displays a map on M5Stack screen. Map can be zoomed in and out with A and C buttons.

