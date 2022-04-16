import math
import os
import random
import re
import logging, time
import sys,logging


# LOGGING DETAILS
logger = logging.getLogger("file")    
logger.setLevel(logging.INFO)

formater = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

fileHandler = logging.FileHandler('file.log')
fileHandler.setFormatter(formater)
logger.addHandler(fileHandler)
logger.info('Opened')
print('*' * 100)
logger.info('Closed')
with open('file.log') as file:
    log = file.read()

    start = re.search(r'opened\s.*\son', log).group().replace('opened ', '').replace(' on', '')
    end = re.search(r'closed\s.*$', log).group().replace('closed ', '')

    print(f'Start: {start} End: {end}')

