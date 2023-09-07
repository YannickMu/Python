from PIL import Image, ImageFont, ImageDraw

def save_compressed(img):
    img.save("../../Desktop/tests/Bilder/test.jpg", "JPEG", omptimize=True, quality=80)

def watermark(img):
    myFont = ImageFont.truetype('arial.ttf', 325,)
    watermarked = ImageDraw.Draw(img)
    watermarked.text((50, 0), "Yannick", font=myFont)


if __name__ == "__main__":
    img = Image.open('../../Bilder/Yanasmagic/2022/def/_DSC5575-13x18.jpg')
    watermark(img)
    save_compressed(img)