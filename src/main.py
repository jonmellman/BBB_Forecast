'''
Created on Aug 17, 2013

@author: jonmellman
'''

from weatherdata import WeatherData
import utils, ledmanager
import os, sys, time

# running in development mode by default
# (development mode bypasses calls to the BBB's IO pins)
developmentMode = True

LOGTAG = os.path.basename(__file__)


def main():
    if not utils.hasInternet():
        utils.log(LOGTAG, 'No internet connection, aborting program.')
        sys.exit()
    
    while True:
        try:
            utils.log(LOGTAG, 'Refreshing forecast data..')
            forecastInfo = fetchForecast()
            forecastText = forecastInfo[0]
            forecastPrecip = forecastInfo[1]
            if not developmentMode:
                textToLED(forecastText)
            time.sleep(60)
        except KeyboardInterrupt:
            ledmanager.cleanUp()
            sys.exit()
        
def fetchForecast():
    forecast = WeatherData()
    fText = forecast.getForecastText()
    utils.log(LOGTAG, 'Retrieved forecast text: ' + fText)
    fPrecip = forecast.getPrecipitation()
    utils.log(LOGTAG, 'Retrieved precipitation value: ' + fPrecip)
    
    fInfo = [fText, fPrecip]
    return fInfo
    
    
def textToLED(text):
    if text == 'Partly Sunny':
        #light yellow
        ledmanager.shineRGB(255, 255, 64)
        pass
    elif text == 'Mostly Sunny':
        #yellow
        ledmanager.shineRGB(255, 255, 0)
        pass
    elif text == 'Sunny':
        #orange
        ledmanager.shineRGB(255, 127, 0)
        pass
    elif text == 'Partly Cloudy':
        #partly cloudy = mostly sunny?
        ledmanager.shineRGB(255, 255, 0)
        pass
    elif text == 'Mostly Cloudy':
        #mostly cloudy = partly sunny?
        ledmanager.shineRGB(255, 255, 64)
        pass
    elif text == 'Cloudy':
        #white
        ledmanager.shineRGB(255, 255, 255)
        pass
    elif text == 'Showers':
        #light blue
        ledmanager.shineRGB(32, 32, 255)
        pass
    elif text == 'Rain / Thunder':
        #blue
        ledmanager.shineRGB(0, 0, 255)
        pass
    elif text == 'Isolated T-Storms':
        #magenta? why not.
        ledmanager.shineRGB(255, 0, 255)
        pass
    elif text == 'N/A':
        #red
        ledmanager.shineRGB(255, 0, 0)
        pass
    else:
        utils.log(LOGTAG, 'Not sure what to do with text: ' + text)
            
if __name__ == '__main__':
    if utils.getSocketHostName() == 'beaglebone':
        developmentMode = False
        utils.log(LOGTAG, 'Starting main method on Beaglebone Black')
    else:
        utils.log(LOGTAG, 'Starting main method in development mode')
        
        
    main()
