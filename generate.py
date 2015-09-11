from PIL import Image, ImageDraw
import numpy as np

def get_center():
    center = np.round(np.random.normal((size[0]/2., size[1]/2.), (100., 100.), 2))
    return center

def get_sigma():
    return (500,500)

def gen_image(name, center, sigma, num, radius):
    size = (1920*2,1800*2)            
    im = Image.new('RGB', size)
    draw = ImageDraw.Draw(im)

    white = (255,255,255)
    black = (0, 0, 0)

    i = 0
    while i < num:
        circle_pos = np.round(np.random.normal(center, sigma, 2))
        circle_box = (circle_pos[0], circle_pos[1], circle_pos[0] + 2*radius, circle_pos[1] + 2*radius)
        draw.ellipse(circle_box, fill = white, outline = black)
        i += 1
    im.save("/Users/dhruv13/Desktop/new/%s.png"%(name), "PNG")

num = 5
radius = 15

num = 20

center = get_center()
sigma = get_sigma()

for i in xrange(1, num + 1):
    gen_image("im%d"%(i), center, sigma, i * 8, radius)