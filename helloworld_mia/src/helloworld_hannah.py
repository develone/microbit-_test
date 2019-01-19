# Write your code here :-)
from microbit import *
name = "Hannah"
while True:
    if button_a.is_pressed():
        display.scroll("HelloWorld ")
        display.scroll(name)
        sleep(1000)
    if button_b.is_pressed():
        display.scroll('HelloWorld', delay=500, wait=True, loop=False, monospace=False)
        display.scroll(name, delay=500, wait=True, loop=False, monospace=False)