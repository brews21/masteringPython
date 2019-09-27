#! /usr/bin/env python3
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

a = 1

def myFunction(val):
    global a
    a = val
    logging.info(a)
    return a


logging.debug(a)
logging.debug(myFunction(2))
logging.debug(a)
