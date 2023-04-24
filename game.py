# Ivy Cobbs - rkg5jw
# Emma Conrod -

import uvage

camera = uvage.Camera(800, 600)

# setting up all the gameboxes and scaling them to the proper size
# Emma: all of these images are saved in the repository :)
background = uvage.from_image(400, 300, "jungle_background.jpeg")
background.size = [800, 600]
sword = uvage.from_image(400, 570, "sword.png")
sword.scale_by(0.2)
heart1 = uvage.from_image(30, 30, "heart.png")
heart1.size = [40, 40]
heart2 = uvage.from_image(70, 30, "heart.png")
heart2.size = [40, 40]
heart3 = uvage.from_image(110, 30, "heart.png")
heart3.size = [40, 40]

# variables that will be referenced in the tick function
lives_left = 3
game_over = False

def tick():
    global lives_left
    global game_over
    camera.draw(background)
    if uvage.is_pressing("left arrow"):
        sword.x -= 5
    if uvage.is_pressing("right arrow"):
        sword.x += 5
    if lives_left >= 1:
        camera.draw(heart1)
    if lives_left >= 2:
        camera.draw(heart2)
    if lives_left == 3:
        camera.draw(heart3)
    if lives_left == 0:
        game_over = True
    camera.draw(sword)
    camera.display()
    

uvage.timer_loop(30, tick)

