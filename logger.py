import os
impot sys
import time
import loggin
from logging.handlers import RotatingFileHandler

def getlogger(program, desc, log_size=104578650):
  logfile=os.path.join(baseloc, '{}_{}.log'.format(program,desc))
  logger=getLogger("testLog")
  logger.setLevel(logging.debug)
  console_handller=logging.StreamHandler()
  console_handller=logging.StreamHandler()
  logging_handler=RotatingFileHandler(log_file,maxBytes-log_size)
  console_handller.setLevl(logging.info)
  console_handller.setLevl(logging.debug)
  console_formatter=logging.Formatter('%(asctime)s-%(message)s')
  console_formatter=logging.Formatter('%(asctime)s-%(message)s')
  console_handler.setFormatter(console_formatter)
  logfile_handler.setFormatter(logfile_formatter)
  logger.addHandler(console_handler)
  logger.addHandler(logfile_handler)
  return logger
  
  
