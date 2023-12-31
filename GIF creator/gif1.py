from moviepy.editor import ImageSequenceClip
from PIL import Image
import numpy as np
from IPython.display import display, Image as IPImage

def resize_image(image_path, new_size):
    img = Image.open(image_path)
    img_resized = img.resize(new_size)
    return img_resized

def pil_to_np(image):
    return np.array(image)

def create_and_display_gif(image_paths, fps=1, target_size=(612, 408)):
    resized_images = [pil_to_np(resize_image(path, target_size)) for path in image_paths]

    clip = ImageSequenceClip(resized_images, fps=fps)
    gif_path = "output.gif"
    clip.write_gif(gif_path, fps=fps)

   
    with open(gif_path, "rb") as f:
        display(IPImage(data=f.read(), format="jpg"))


image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
create_and_display_gif(image_paths, fps=0.5)
