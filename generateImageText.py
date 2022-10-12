from PIL import Image, ImageDraw, ImageFont
from random import randint, choice

c1 = randint(0, 256)
c2 = randint(0, 256)
c3 = randint(0, 256)
c4 = randint(0, 256)
c5 = randint(0, 256)
c6 = randint(0, 256)


txt2 = input("Text: ")

colorss = ["black", "Azure", "Chocolate", "DarkGray", "Gray", "DarkTurquoise",
           "Gainsboro", "GhostWhite", "HoneyDew", "green", "blue", "red"]
col = choice(colorss)

img = Image.new('RGB', (1936, 1936), color=f'{col}')
fnt = ImageFont.truetype("Mermaid.ttf", 1300)
fnt2 = ImageFont.truetype("Ft.ttf", 70)
fnt3 = ImageFont.truetype("Bebas.ttf", 1500)
draw = ImageDraw.Draw(img)

draw.text(xy=(0, 100), text=f'{str(txt2.upper())[3:8]}', fill=(
    c6, c3, c1), font=fnt3)
draw.text(xy=(0, 1100), text=f'{txt2}', fill=(c4, c5, c6), font=fnt)
draw.text(xy=(50, 200), text=f'{" ".join(str(txt2.upper()))[10:]}', fill=(
    c1, c2, c3), font=fnt2)


img.save('Output.jpg')

print("Done!")
