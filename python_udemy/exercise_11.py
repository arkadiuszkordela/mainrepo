# In this exercise I have to make a program to show for a user height and weight of the image from source. 

from PIL import Image

def show_image_dimensions(image_path):
    image = Image.open(image_path)
    width, height = image.size
    print(f'The image is {width} pixels wide and {height} pixels tall.')

show_image_dimensions('image.jpg')