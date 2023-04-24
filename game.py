# Ivy Cobbs - rkg5jw
# Emma Conrod - eup2fs

# Description: The user is a "good guy" in a jungle fighting a team of ninjas, which fly down from the trees
# and also drop bombs from above that must be avoided. You can hit the ninjas--which awards points--by moving
# the sword across the bottom of the screen. If you hit a bomb, you lose a life. There are also stars that fall along
# with the ninjas and bombs, and collecting a star awards one additional life.

# 3 basic features: user input, game over, and graphics
#   user input: the user can move the sword by pressing the left and right arrow keys.
#   game over: when you hit so many bombs that you run out of lives, the game ends.
#   graphics: we use images from the web, saved locally, to create gameboxes for the sword, ninjas, bombs, health bar,
#   stars, and jungle background.

# 4 additional features: restart from game over, enemies, collectables, and health bar
#   restart from game over: when the game ends, the user has the option to restart gameplay by pressing the space bar
#   enemies: the falling ninjas are the enemies that the user should "hit" in order to gain points
#   collectables: the stars that fall down add one life to the user's health bar when "collected"
#   health bar: the health bar appears at the top of the screen in the form of red hearts, one for each "life" the
#   player has left. When the player gets a star, an additional heart appears, when they hit a ninja, one heart
#   disappears, and when there are no hearts left, the game ends.

# everything below is new as of Checkpoint 2.

import uvage

camera = uvage.Camera(800, 600)

# some of the variables that will be referenced in the tick function
lives_left = 3
game_over = False
points = 0
clock = 0  # I haven't written code for this in the function yet, but I was thinking we could use it to tell the game
# which baddie to spawn at a given moment. Like every x amount of time, we can cycle through the same pattern of baddies
# falling from the top

# setting up all the gameboxes and scaling them to the proper size. All of these images are saved in the repository :)
background = uvage.from_image(400, 300, "jungle_background.jpeg")
background.size = [800, 600]
sword = uvage.from_image(400, 560, "sword.png")
sword.scale_by(0.15)
sword.speedx = 0
sword.speedy = 0
star1 = uvage.from_image(200, -30, "star.png")
star1.scale_by(0.1)
star2 = uvage.from_image(400, -30, "star.png")
star2.scale_by(0.1)
star3 = uvage.from_image(600, -30, "star.png")
star3.scale_by(0.1)
stars = [star1, star2, star3]
ninja1 = uvage.from_image(100, -30, "baddie.png")
ninja1.scale_by(0.2)
ninja2 = uvage.from_image(150, -30, "baddie.png")
ninja2.scale_by(0.2)
ninja3 = uvage.from_image(200, -30, "baddie.png")
ninja3.scale_by(0.2)
baddies = [ninja1, ninja2, ninja3]
heart1 = uvage.from_image(30, 30, "heart.png")
heart1.size = [40, 40]
heart2 = uvage.from_image(70, 30, "heart.png")
heart2.size = [40, 40]
heart3 = uvage.from_image(110, 30, "heart.png")
heart3.size = [40, 40]


def tick():
    global lives_left
    global game_over
    global points
    global clock
    camera.draw(background)
    clock += 1
    score = uvage.from_text(750, 30, str(points), 35, "red")
    for ninja in baddies:
        if not game_over:
            ninja.y += 5
        if ninja.bottom_touches(sword, 0, -10):
            points += 1
            ninja.y = -30
        if ninja.y >= 580:
            ninja.y = -30
    for star in stars:
        if not game_over:
            star.y += 5
        if star.touches(sword):
            if lives_left < 3:
                lives_left += 1
            star.y = -30
        if star.y >= 590:
            star.y = -30
    if uvage.is_pressing("left arrow") and sword.x >= 38:
        sword.move_speed()
        if sword.speedx >= -10:
            sword.speedx -= 1
    if uvage.is_pressing("right arrow") and sword.x <= 762:
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
# here is probably where we will add more draw statements to show the falling stars and ninjas
    camera.draw(score)
    camera.draw(sword)
    camera.display()


uvage.timer_loop(30, tick)
