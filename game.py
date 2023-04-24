# Ivy Cobbs - rkg5jw
# Emma Conrod -

import uvage

camera = uvage.Camera(800, 600)

# variables that will be referenced in the tick function
lives_left = 3
game_over = False
points = 0
clock = 0  # I haven't written code for this in the function yet but I was thinking we could use it to tell the game 
# which baddie to spawn at a given moment. Like every x amount of time, we can cycle through the same pattern of baddies
# falling from the top

# setting up all the gameboxes and scaling them to the proper size
# Emma: all of these images are saved in the repository :)
background = uvage.from_image(400, 300, "jungle_background.jpeg")
background.size = [800, 600]
sword = uvage.from_image(400, 560, "sword.png")
sword.scale_by(0.15)
sword.speedx = 0
sword.speedy = 0
baddie1 = uvage.from_image(100, -30, "baddie.png")
baddie1.scale_by(0.2)
baddie2 = uvage.from_image(150, -30, "baddie.png")
baddie2.scale_by(0.2)
baddie3 = uvage.from_image(200, -30, "baddie.png")
baddie3.scale_by(0.2)
heart1 = uvage.from_image(30, 30, "heart.png")
heart1.size = [40, 40]
heart2 = uvage.from_image(70, 30, "heart.png")
heart2.size = [40, 40]
heart3 = uvage.from_image(110, 30, "heart.png")
heart3.size = [40, 40]
score = uvage.from_text(750, 30, str(points), 35, "red")


def tick():
    global lives_left
    global game_over
    global points
    global clock
    camera.draw(background)
    clock += 1
    if not game_over:
        baddie1.y += 5
    if baddie1.bottom_touches(sword, 0, -10):
        points += 1
        baddie1.y = -30
    if uvage.is_pressing("left arrow"):
        sword.move_speed()
        if sword.speedx >= -10:
            sword.speedx -= 1
    if uvage.is_pressing("right arrow"):
        sword.move_speed()
        if sword.speedx <= 10:
            sword.speedx += 1
    if not uvage.is_pressing("right arrow") and not uvage.is_pressing("left arrow"):
        sword.speedx = 0
    if lives_left >= 1:
        camera.draw(heart1)
    if lives_left >= 2:
        camera.draw(heart2)
    if lives_left == 3:
        camera.draw(heart3)
    if lives_left == 0:
        game_over = True
    camera.draw(score)
    camera.draw(baddie1)
    camera.draw(sword)
    camera.display()


uvage.timer_loop(30, tick)

