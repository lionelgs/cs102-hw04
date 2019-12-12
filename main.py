import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

for i in range(1, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (255-r, 255-g, 255-b))

new_img.save(output_path, "JPEG")
