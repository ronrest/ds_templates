import PIL as pil
def show_img(a):
    """Given a numpy array representing an image, view it"""
    img = pil.Image.fromarray(a)
    img.show()
