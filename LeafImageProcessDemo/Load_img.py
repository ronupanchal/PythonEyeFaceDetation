from PIL import Image


image = Image.open('cat.jpg')
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_image1.jpg')