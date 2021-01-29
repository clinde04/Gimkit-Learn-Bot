#!/usr/bin/env python3

import os
import sys
from gimkit import *

if __name__ == '__main__':
  if os.environ.get("CODE") != None:
    code = os.environ.get("CODE")
  else:
    codeinput = input('Enter the game code: ')
    code = codeinput
  if os.environ.get("NAME") != None:
    name = os.environ.get("NAME")
  else:
    nameinput = input('What name would you like to use:')
    name = nameinput
  join_game(code, name)
  play()
