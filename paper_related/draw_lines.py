import math
from PIL import Image, ImageDraw

im = Image.open("pl_deep.png")
im.show()

line = ImageDraw.Draw(im)

# Line 1
coords = [(90, 85), (136, 85)]
line.line(coords, fill = 128, width = 3)
coords = [(136, 85), (136, 432)]
line.line(coords, fill = 128, width = 3)

# Line 2
coords = [(90, 116), (188, 116)]
line.line(coords, fill = 128, width = 3)
coords = [(188, 116), (188, 432)]
line.line(coords, fill = 128, width = 3)

# Line 3
coords = [(90, 150), (248, 150)]
line.line(coords, fill = 128, width = 3)
coords = [(248, 150), (248, 432)]
line.line(coords, fill = 128, width = 3)

# Line 4
coords = [(90, 192), (318, 192)]
line.line(coords, fill = 128, width = 3)
coords = [(318, 192), (318, 432)]
line.line(coords, fill = 128, width = 3)

# Line 5
coords = [(90, 240), (400, 240)]
line.line(coords, fill = 128, width = 3)
coords = [(400, 240), (400, 432)]
line.line(coords, fill = 128, width = 3)

# Line 6
coords = [(90, 298), (500, 298)]
line.line(coords, fill = 128, width = 3)
coords = [(500, 298), (500, 432)]
line.line(coords, fill = 128, width = 3)

# Line 7
coords = [(90, 374), (628, 374)]
line.line(coords, fill = 128, width = 3)
coords = [(628, 374), (628, 432)]
line.line(coords, fill = 128, width = 3)

im.show()

im = im.save("pl_deep_new.png")