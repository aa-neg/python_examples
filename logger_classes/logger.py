import logging, logging.handlers
import os
import sys
import traceback
import __main__ as main

logging.getLogger().setLevel(logging.INFO)
# Send to terminal
logging.propagate = False

filename= './logs/s3_synapse.log'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler(filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('This is a test log message.')

