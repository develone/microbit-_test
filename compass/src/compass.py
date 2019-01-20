from microbit import *

compass.calibrate()

tardiscompass = 0

while True:
    if button_b.is_pressed():
        tardiscompass = compass.heading()
        if tardiscompass >= 0:
            display.scroll("Lower")
        elif tardiscompass <= 10:
            display.scroll("Higher")
    if button_a.is_pressed():
        tardiscompass = compass.heading()
        if 0 < tardiscompass < 30:
            display.scroll("Point 0 to 30")
        elif 30 < tardiscompass < 60:
            display.scroll("30 to 60")
        elif 60 < tardiscompass < 90:
            display.scroll("60 to 90")        
        elif 90 < tardiscompass < 120:
            display.scroll("90 to 120")
        if 120 < tardiscompass < 150:
            display.scroll("120 to 150")
        elif 150 < tardiscompass < 180:
            display.scroll("150 to 180")
        elif 150 < tardiscompass < 180:
            display.scroll("150 to 180")        
        elif 180 < tardiscompass < 210:
            display.scroll("180 to 210")

        elif 210 < tardiscompass < 240:
            display.scroll("210 to 240")
        elif 240 < tardiscompass < 270:
            display.scroll("240 to 270")
        elif 270 < tardiscompass < 300:
            display.scroll("270 to 300")        
        elif 300 < tardiscompass < 330:
            display.scroll("300 to 330")
        else: 
            display.scroll("330 to 360")
    else:
        display.scroll("?")
    
        
            