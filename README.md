BBB_Forecast
============

# Description

Using the [BeagleBone Black microcomputer](http://beagleboard.org/Products/BeagleBone%20Black), shine different colored LEDs depending on the weather forecast.

# Depencencies

The [pywapi](https://code.google.com/p/python-weather-api/) library is used to fetch the weather data and the [Adafruit_BBIO.PWM](https://github.com/adafruit/adafruit-beaglebone-io-python) library  is used to control the LEDs.

# Circuit

Setting up the physical circuit is straightforward; the only components are an RGB LED and four jumper wires. (Probably should use some resistors, but my LED's are cheap and plentiful.)
* Jumper wire from P8_13 to the LED's red lead
* Jumper wire from P8_19 to the LED's green lead
* Jumper wire from P9_14 to the LED's blue lead
* Jumper wire from P8_2 to the LED's negative lead

# Usage

Simply run main.py after wiring up the circuit.

# Weather color codes (work in progress)
| Color           | Forecast Info |
| -------------   | ------------- |
| Pale Yellow     | Partly Sunny/Mostly Cloudy    |
| Yellow          | Mostly Sunny/Partly Cloudy    |
| Orange          | Sunny                         |
| White           | Cloudy                        |
| Pale Blue       | Showers                       |
| Blue            | Rain / Thunder                |
| Magenta         | Isolated T-Storms             |
| Red             | N/A                           |
