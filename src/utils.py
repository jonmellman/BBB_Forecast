'''
Contains utilities for logging purposes, to check
internet connection, and to obtain platform information.

Created on Aug 18, 2013

@author: jonmellman
'''

import logging
import socket
import urllib2

logInitialized = False


def logInit():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    logInitialized = True

def log(logtag, text):
    if not logInitialized:
        logInit()
        
    logging.info(logtag + ": " + text)

    
def getSocketHostName():
    return socket.gethostname()

def hasInternet():
    try:
        #check a google IP address, timeout after 1 second
        response=urllib2.urlopen('http://www.google.com',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False