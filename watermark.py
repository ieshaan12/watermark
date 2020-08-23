from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

def waterMarkImages(imageInputPath, fileName, imageOutputPath, text, fontPath):
    photo = Image.open(imageInputPath + '\\' + fileName)

    w, h = photo.size

    fontsize = min(w,h) // 65

    drawing = ImageDraw.Draw(photo)

    font = ImageFont.truetype(fontPath, fontsize)


    text_w, text_h = drawing.textsize(text, font)

    pos = w - text_w - w//100, (h - text_h) - h//100


    drawing.text(pos, text, fill="#ffffff", font=font)

    photo.save(outputFolder + '\\' + fileName)

if __name__ == "__main__":
    folder = "C:\\Users\\Work\\Desktop\\photos"
    outputFolder= "C:\\Users\\Work\\Desktop\\VSCode\\ieshaan12.github.io\\images\\Gallery"
    font = "C:\\Users\\Work\\Desktop\\VSCode\\ieshaan12.github.io\\fonts\\Bangers-Regular.ttf"

    text = "© Ieshaan Saxena"
    print(folder)
    print(outputFolder)
    print(os.getcwd())

    if os.path.exists(folder):
        for i in os.listdir(folder):
            waterMarkImages(folder, i, outputFolder, text, font)
    else:
        print("Invalid path")  
        os._exit(0)