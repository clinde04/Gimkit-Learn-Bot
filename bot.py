#!/usr/bin/env python3

import os
import sys
from gimkit import *



if __name__ == '__main__':
  if os.environ.get("CODE") != None:
    code = os.environ.get("CODE")
  else:
    code = input('What is da fking code bro? > ')\

  if os.environ.get("NAME") != None:
    name = os.environ.get("NAME")
  else:
    name = input ('Da fk is ur name homie? > ')
  
  join_game(code, name)
  play()
