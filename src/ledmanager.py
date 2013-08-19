'''
Created on Aug 17, 2013

@author: jonmellman
'''

import utils
if utils.getSocketHostName() == 'beaglebone':
    import Adafruit_BBIO.PWM as PWM  # @UnresolvedImport
import time
    
PIN_RED = "P8_13"
PIN_GREEN = "P8_19"
PIN_BLUE = "P9_14"

# blue overpowers green and both vastly
# overpower red - compensate by restricting
# green and blue's maximum duty cycle

MAXIMUMS = [0, 50, 60]
REDMAX = 0
GREENMAX = 50
BLUEMAX = 60

def shineRGB(red, green, blue, blinkFrequency=0):
    PWM.start(PIN_RED, 100)
    PWM.start(PIN_GREEN, 100)
    PWM.start(PIN_BLUE, 100)
    
    rawValues = [red, green, blue]
    convertedValues = _convertValues(rawValues)
    
    PWM.set_duty_cycle(PIN_RED, convertedValues[0])
    PWM.set_duty_cycle(PIN_GREEN, convertedValues[1])
    PWM.set_duty_cycle(PIN_BLUE, convertedValues[2])

def cleanUp():
    PWM.start(PIN_RED, 100)
    PWM.start(PIN_GREEN, 100)
    PWM.start(PIN_BLUE, 100)
    
    PWM.stop(PIN_RED)
    PWM.stop(PIN_BLUE)
    PWM.stop(PIN_GREEN)
    
def _convertValues(rawVals):
    '''
    Convert 0-255 color values into duty cycles,
    restricted by the color's max duty cycle.
    
    e.g. blue value of 255 (full blue) gets
    converted to 60, as 60 is the maximum
    duty cycle we've restricted blue to
    
    '''
    results = []
    
    # first, scale the values so they're in the range (0, 255)
    for color in rawVals:
        results.append((100/255) * color)
    
    # next, we invert (higher duty cycle = less power) and
    # scale again so its within the range (MAXIMUM, 100)
    # (duty cycle of 100 is totally off)
    for i in range(0, 3):
        results[i] = ((MAXIMUMS[i] - 100) / 100) * results[i] + 100
    
    return results  