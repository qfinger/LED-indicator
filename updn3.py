import urllib
import time

#Repeatedly pull quote and determine if it is positive or negative
repeat = "y"
while repeat == "y":
    fhand = urllib.urlopen('http://finance.yahoo.com/d/quotes.csv?s=^AORD&f=p2')
    for line in fhand:
        nums = len(line)
        numline = line [1:nums - 3]  #-newline, quotation mark and percent sign
        numfloat = float(numline)
        print numfloat
    
        if numfloat < 0:
            print 'The market is down', numfloat, 'percent.'
            print ""
        else:
            print 'The market is up', numfloat, 'percent.'
            print ""
       

#optional delay
#time.sleep(2)     
           
    #unicorn hat matrix color change based on market direction
    #put all this into a function, as well as mkt open and close displays?
    import unicornhat as unicorn
    from random import randint
    import time

    #tie LED brightness to change magnitude here
    #and direction: if numfloat < 0 make direction down
    unicorn.brightness(0.30)
    
    if numfloat < 0:
        unicorn.rotation(180)
    else:
        unicorn.rotation(90)

    #colors if market is up, down,or zero change
    if numfloat > 0:
        wrd_rgb = [[154, 173, 154], [0, 255, 0], [0, 200, 0], [0, 162, 0], [0, 145, 0], [0, 96, 0], [0, 74, 0], [0, 0, 0,]]
    elif numfloat < 0:
        wrd_rgb = [[255, 20, 20], [245, 10, 10], [200, 0, 10], [162, 0, 0], [145, 0, 0], [96, 0, 0], [74, 0, 0], [0, 0, 0,]]
    else:     #maybe change this to rainbow sparkles
        wrd_rgb = [[255, 193, 37], [238, 180, 34], [205, 155, 29], [139, 105, 20], [120, 85, 10], [100, 65, 5], [50, 30, 5], [0, 0, 0,]]

    clock = 0

    blue_pilled_population = [[randint(0,7), 7]]
 
    #while True:
    timeout_start = time.time()

# timeout variable can be omitted, if you use specific value in the while condition
    timeout = 10   # [seconds]

    while time.time() < timeout_start + timeout:
        test = 0
        if test == 5:
            break
        test = test - 1
            
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
   
    #end of unicorn loop

      # NEXT STEPS: reverse direction depending on up or down
      #Also consider flashing a rainbow or sprite when market changes direction
      #Also consider indicating magnitude of up or down with speed or brightness
      #Also consider doing sparkly rainbows for 10 seconds at opening closing bell
      #Do a yield curve one?  
