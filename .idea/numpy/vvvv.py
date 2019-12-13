from PIL import Image

from resizeimage import resizeimage

with open('/home/bmaharjan/Desktop/thor2.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [200, 100], validate=False)
        cover.save('/home/bmaharjan/Desktop/test-image-cover.jpeg', image.format)
