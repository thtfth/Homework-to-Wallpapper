from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def text_to_image(text):
    def getSize(txt, font):
        testImg = Image.new('RGB', (1, 1))
        testDraw = ImageDraw.Draw(testImg)
        return testDraw.textsize(txt, font)

    if __name__ == '__main__':

        fontname = "arial.ttf"
        fontsize = 30

        colorText = "black"
        colorOutline = "white"
        colorBackground = "white"


        font = ImageFont.truetype(fontname, fontsize)
        width, height = getSize(text, font)
        img = Image.new('RGB', (width+1920, height+1080), colorBackground)
        d = ImageDraw.Draw(img)
        d.text((750, height/2), text, fill=colorText, font=font)
        d.rectangle((0, 0, width+1920, height+1080), outline=colorOutline)
    
        img.save(r'C:\Users\l.e.yu\Desktop\CLICK HERE TO RECORD UR HOMEWORK\test1.png')

f = open('test.txt', 'r')

text_to_image(f.read())

#omg that part is finally done.
