# -*- coding: utf-8 -*-
#Flood Fill Algorithm
from IPython.core.display import display_latex
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

def is_valid(screen, m, n, x, y, old_colour, new_colour):
  if(x<0 or x>=m or y<0 or y>= n or screen[x][y]!= old_colour or screen [x][y] == new_colour):
    return False
  return True
    

def flood_fill(screen, m, n, x, y, old_colour, new_colour):
    queue = []

    queue.append([x, y])
    screen[x][y] = new_colour

    while queue:

      current_pixel = queue.pop()

      x_position = current_pixel[0]
      y_position = current_pixel[1]

      if(is_valid(screen, m, n, x_position+1, y_position, old_colour, new_colour)):
        screen[x_position + 1][y_position] = new_colour
        queue.append([x_position+1, y_position])

      if(is_valid(screen, m, n, x_position-1, y_position, old_colour, new_colour)):
        screen[x_position - 1][y_position] = new_colour
        queue.append([x_position-1, y_position])

      if(is_valid(screen, m, n, x_position, y_position+1, old_colour, new_colour)):
        screen[x_position][y_position+1] = new_colour
        queue.append([x_position, y_position+1])

      if(is_valid(screen, m, n, x_position, y_position-1, old_colour, new_colour)):
        screen[x_position][y_position-1] = new_colour
        queue.append([x_position, y_position-1])


def main():
  screen =[
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 0],
  [1, 0, 0, 1, 1, 0, 1, 1],
  [1, 2, 2, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 2, 2, 0],
  [1, 1, 1, 1, 1, 2, 1, 1],
  [1, 1, 1, 1, 1, 2, 2, 1],
    ]

  m = len(screen)
  n = len(screen[0])

  x = 4
  y = 4

  old_colour = screen[x][y]
  new_colour = 2

  flood_fill(screen, m, n, x, y, old_colour, new_colour)

  for i in range(m):
    for j in range(n):
      print(screen[i][j], end =' ')
    print()

main()
