from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
import getch
from gfxhat import backlight
from gfxhat import lcd
import gfxhat
from gfxhat import lcd
import click
#Etch-a-sketch
# Displays the text "etch-a-sketch"
def displayText(text,lcd,a,b):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 18)
    w, h = font.getsize(text)
    draw.text((a,b), text, 1, font)
    for x1 in range(a,a+w):
        for y1 in range(b,b+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

# Etching

def etcha():
    x = 1
    y = 63
    lcd.set_pixel(x,y,1)
    print ('start')
    lcd.show() #sets the intial point to bottom left
    running = True
    while running == True:
        char = click.getchar()
        if char == '\x1b[A': #UP
            y = y - 1
            if y == 0:
                y = 63
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif char == '\x1b[B': #DOWN
            y = y + 1
            if y == 64:
                y = 1
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif char == '\x1b[C': #RIGHT
            x = x + 1
            if x == 128:
                x = 1
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif char == '\x1b[D': #LEFT
            x = x - 1
            if x == 0:
                x =127
            lcd.set_pixel(x,y,1)
            lcd.show() 
        elif char == 'q':
            running = False
        elif char == 's':
            lcd.clear()
            lcd.show()
            text = "etch-a-sketch"
            displayText(text,lcd,25,-5)

def displayObject(obj,xx,yy):  
    x = xx
    y = yy
    a = 0
    while a <= len(obj) - 1: 
        b = 0 
        while b <= len(obj[a]) - 1:
            p = obj[a][b]
            lcd.set_pixel(x,y,p)
            x += 1
            b += 1
        x = xx
        y += 1
        a += 1
    lcd.show()
