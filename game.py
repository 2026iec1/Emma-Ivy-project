# Ivy Cobbs - rkg5jw
# Emma Conrod -

import uvage

background_link = "jungle_background.png"
camera = uvage.Camera(800, 600, )
sword = uvage.from_image(400, 580, "file_name")


def tick():
    if uvage.is_pressing("left arrow"):
        sword.x -= 5
    if uvage.is_pressing("right arrow"):
        sword.x += 5

