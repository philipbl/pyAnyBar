#!/usr/bin/env python

from time import sleep
from anybar import AnyBar

ab = AnyBar()

def change(color):
    ab.change(color)
    sleep(.5)

change('white')
change('red')
change('orange')
change('yellow')
change('green')
change('cyan')
change('blue')
change('purple')
change('black')
change('question')
change('exclamation')

try:
    change('fdafsd')
except ValueError:
    pass
