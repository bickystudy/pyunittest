import os
import sys
import argparse
import subprocess

def get_options(args)
  parser=argparse.ArgumentParser(description="Test Code")
  parser.add_argument('-E', action='store', dest='env', type=str, help='environment')
  cmd_args=parser.parse_args(args)
  return cmd_args
  
def initiali(env)
  logger.info("STarted")
  data_var={}
  data_var['now']=datetime.now()
  data_var['env']=env
  return data_var
  
main(args)
  arg_parse=get_option(args)
  
  global logger
  logger=getlogger("Testt",arg_parse.env)
  logger.info("Profile set")
  
  data_variable=initiali(arg_parse.env)
  
