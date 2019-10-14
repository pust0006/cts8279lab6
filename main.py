from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw
import library
backlight.set_all(140, 0, 0)
lcd.clear()
lcd.show()
backlight.show()
print ("This program has 2 functions")
print ("1. Etch a sketch using arrow keys")
print ("2. Prints an image on screen")
print ("3. Closes the program")
text = "etch-a-sketch"
running2 = True

f = [#image one
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]
p = [[0,0,0,1,1,1,1,1,0,0,0],#image 2
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

while running2 == True:
    numb = input("Enter the program number: ")
    if numb == '1':
        xx = 25
        yy = -5
        lcd.clear()
        lcd.show()
        library.displayText(text,lcd,xx,yy)
        library.etcha()
    elif numb == '2':
        lcd.clear()
        lcd.show()
        print ('There are two objects')
        numb = (input("1 or 2: "))
        if numb == '1':
            obj = f
        elif numb == '2':
            obj = p
        xx = int(input("x coordinate: "))
        yy = int(input("y coordinate: "))
        library.displayObject(obj,xx,yy)
    elif numb == '3':
        running2 = False