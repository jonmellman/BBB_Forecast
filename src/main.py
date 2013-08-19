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
        utils.log(LOGTAG, 'Refreshing forecast data..')
        forecastInfo = fetchForecast()
        forecastText = forecastInfo[0]
        forecastPrecip = forecastInfo[1]
        if not developmentMode:
            textToLED(forecastText)
        time.sleep(60)
        
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
        pass
    elif text == 'Mostly Sunny':
        pass
    elif text == 'Sunny':
        pass
    elif text == 'Partly Cloudy':
        pass
    elif text == 'Mostly Cloudy':
        pass
    elif text == 'Cloudy':
        pass
    elif text == 'Showers':
        pass
    elif text == 'Rain / Thunder':
        pass
    elif text == 'N/A':
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