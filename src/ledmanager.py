'''
Created on Aug 17, 2013

@author: jonmellman
'''

import utils
if utils.getSocketHostName() == 'beaglebone':
    import Adafruit_BBIO.PWM as PWM  # @UnresolvedImport
import time


class LEDManager(object):
    '''
    Contains methods to control the color,
    '''
    
    RED = "P8_13"
    GREEN = "P8_19"
    BLUE = "P9_14"
    
    REDMAX = 0
    GREENMAX = 50
    BLUEMAX = 60
    
    @staticmethod
    def shineColor(red, green, blue, blinkFrequency=0):
        PWM.start(LEDManager.RED, 100)
        PWM.start(LEDManager.GREEN, 100)
        PWM.start(LEDManager.BLUE, 100)
        
        PWM.set_duty_cycle(LEDManager.RED, LEDManager._convertValue(red))
        PWM.set_duty_cycle(LEDManager.GREEN, LEDManager._convertValue(green))
        PWM.set_duty_cycle(LEDManager.BLUE, LEDManager._convertValue(blue))
    
    @staticmethod
    def cleanUp():
        PWM.start(LEDManager.RED, 100)
        PWM.start(LEDManager.GREEN, 100)
        PWM.start(LEDManager.BLUE, 100)
        
        PWM.stop(LEDManager.RED)
        PWM.stop(LEDManager.BLUE)
        PWM.stop(LEDManager.GREEN)
    
    @staticmethod
    def _convertValue(val):
        '''
        Convert 0-255 color value into a duty cycle,
        restricted by the color's maximum
        '''
        
        return val

    def __init__(self):
        '''
        Constructor
        '''
        