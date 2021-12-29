import sys
import os
from os import system

try:
  import requests
except ImportError:
  system('pkg install ruby')
  system('gem install lolcat')
  system('clear')
  print("Run it again!\n")
  sys.exit()

try:
  system('clear')
  system('sl | lolcat')
except:
   KeyboardInterrupt()
