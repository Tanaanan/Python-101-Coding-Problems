RGB = list(input("").split(" "))
R = int(RGB[0])
G = int(RGB[1])
B = int(RGB[2])



def color(colour):
    if colour > 255:
        colour = 255
    elif colour < 0:
        colour = 0

    colour = hex(colour)[2:].upper()
    if len(colour) < 2:
        colour = "0"+colour
    return colour

def rgb(r,g,b):
    print(color(r)+color(g)+color(b))

rgb(R,G,B)
    