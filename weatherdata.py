'''
The weatherdata module provides a 
WeatherData object, which uses the pywapi module to
facilitate the retrieval of weather attributes.

Created on Aug 17, 2013

@author: jonmellman
'''

import pywapi
import datetime
import logging

class WeatherData(object):
    '''
    A WeatherData object allows for the retrieval of weather
    attributes, 
    '''
    # hour after which tomorrow's forecast will be requested instead of today's
    requestDayCutoffHour = 12 
    
    # set up logger's timestamp
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


    def __init__(self, zipCode='29613'):
        '''
        Constructor
        '''
        self.zipCode = zipCode
        self.weatherData = pywapi.get_weather_from_weather_com(self.zipCode, 'imperial') 
        
        # used in WeatherData's get methods, so we know what index of
        # the forecast list we want
        self.requestDayIndex = self._getRequestDayIndex()
        
    def getForecastText(self):
        '''
        Returns text e.g. 'Showers', 'Mostly Sunny', etc.
        '''
        return str(self.weatherData['forecasts'][self.requestDayIndex]['day']['text'])
    
    def getPrecipitation(self):
        '''
        Returns a string representing the chance of precipitation
        '''
        return str(self.weatherData['forecasts'][self.requestDayIndex]['day']['chance_precip'])

    def _chooseRequestDay(self):
        '''
        Called by _getRequestDayIndex(), this
        determines what day to fetch the forecast
        for, based on the requestDayCutoffHour   
        '''
        if datetime.datetime.now().hour >= WeatherData.requestDayCutoffHour:
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            logging.info('It\'s afternoon. Getting forecast for: ' + str(tomorrow))
            return tomorrow.day
        else:
            today = datetime.date.today()
            logging.info('It\'s before noon. Getting forecast for: ' + str(today))
            return today.day
            
    def _getRequestDayIndex(self):
        '''
        Returns the index of
        '''
        requestDay = self._chooseRequestDay()
        for i in range(0, 4): #forecast list has five elements
            forecastDate = str(self.weatherData['forecasts'][i]['date'])
            forecastDay = int(forecastDate[-2:]) #Snip the month prefix
            if forecastDay == requestDay:
                return i
