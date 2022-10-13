from PIL import Image, ImageDraw, ImageFont
from random import randint, choice

c1 = randint(0, 256)
c2 = randint(0, 256)
c3 = randint(0, 256)
c4 = randint(0, 256)
c5 = randint(0, 256)
c6 = randint(0, 256)

print("=======Custom Name========\n")
firstName = input("First Name: ")
lastName = input("Last Name :")


colors = ["black", "Azure", "Chocolate", "DarkGray", "Gray", "DarkTurquoise",
           "Gainsboro", "GhostWhite", "HoneyDew", "green", "blue", "red"]
col = choice(colors)

img = Image.new('RGB', (1024, 768), color=f'{col}')
fnt = ImageFont.truetype("Mermaid.ttf", 200)
fnt2 = ImageFont.truetype("Ft.ttf", 200)
fnt3 = ImageFont.truetype("Bebas.ttf", 200)
draw = ImageDraw.Draw(img)

draw.text(xy=(100, 200),fill=(c6, c3, c1), text = firstName, font=fnt3)
draw.text(xy=(200, 300),fill=(c4, c5, c6), text= lastName ,font=fnt)



img.save('Output.jpg')

print("Done!")
