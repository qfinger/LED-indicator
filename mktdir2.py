import urllib
import time

#Repeatedly pull SPY quote and determine if it is positive or negative
repeat = "y"
while repeat == "y":
    fhand = urllib.urlopen('http://finance.yahoo.com/d/quotes.csv?s=SPY&f=p2')
    for line in fhand:
        print line.strip()
    

    change = line
    count = 0
    for letter in change:
        if letter == "-":
            count = count + 1

    if count > 0:
        print 'The market is down.'
    else:
        print 'The market is up.'
    

#unicorn hat matrix color change based on market direction

    import unicornhat as unicorn
    from random import randint
    import time

    unicorn.brightness(0.20)
    unicorn.rotation(90)

    if count < 1:
        wrd_rgb = [[154, 173, 154], [0, 255, 0], [0, 200, 0], [0, 162, 0], [0, 145, 0], [0, 96, 0], [0, 74, 0], [0, 0, 0,]]
    else:
        wrd_rgb = [[255, 173, 154], [255, 0, 0], [200, 0, 0], [162, 0, 0], [145, 0, 0], [96, 0, 0], [74, 0, 0], [0, 0, 0,]]

    clock = 0

    blue_pilled_population = [[randint(0,7), 7]]
    while True:
          for person in blue_pilled_population:
                    y = person[1]
                    for rgb in wrd_rgb:
                            if (y <= 7) and (y >= 0):
                                   unicorn.set_pixel(person[0], y, rgb[0], rgb[1], rgb[2])
                            y += 1
                   person[1] -= 1
         unicorn.show()
          time.sleep(0.1)
          clock += 1
           if clock % 5 == 0:
                   blue_pilled_population.append([randint(0,7), 7])
           if clock % 7 == 0:
                blue_pilled_population.append([randint(0,7), 7])
           while len(blue_pilled_population) > 100:
                   blue_pilled_population.pop(0)
                   
    
 #wait 10 seconds before repeating
    time.sleep(10)