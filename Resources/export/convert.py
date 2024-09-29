import os

for img in os.listdir():
    print(img)
    os.system("magick ./{} ./convert/{}".format(img, img.replace(".png", ".dds")))