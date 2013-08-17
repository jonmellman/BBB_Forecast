'''
Created on Aug 17, 2013

@author: jonmellman
'''

from weatherdata import WeatherData
from ledmanager import LEDManager

def main():
    forecast = WeatherData()
    fText = forecast.getForecastText()
    fPrecip = forecast.getPrecipitation()
    
    print fText
    textToLED(fText)
    
def textToLED(text):
    splitText = text.split()
    if len(splitText) == 2:
        #text contains descriptor e.g. "Mostly Cloudy"
        if splitText[0] == 'Partly':
            #deal with Partly
            pass
        elif splitText[0] == 'Mostly':
            #deal with mostly
            pass
        else:
            print 'New descriptor found: ' + splitText[0]
    
    if splitText[-1] == 'Sunny':
        LEDManager.shineColor(0, 50, 100)
        pass
    if splitText[-1] == 'Cloudy':
        LEDManager.shineColor(0, 50, 60)
        pass
    if splitText[-1] == 'Showers':
        LEDManager.shineColor(100, 100, 60)
        pass
            
        
    
    

if __name__ == '__main__':
    main()