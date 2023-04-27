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
falling = {"ninja1": True, "ninja2": False, "ninja3": False, "ninja4": False, "star1": False, "star2": False,
           "bomb1": False, "bomb2": False}

# setting up all the gameboxes and scaling them to the proper size.
background = uvage.from_image(400, 300, "jungle_background.jpeg")
background.size = [800, 600]
sword = uvage.from_image(400, 560, "sword.png")
sword.scale_by(0.15)
star1 = uvage.from_image(200, -30, "star.png")
star1.scale_by(0.1)
star2 = uvage.from_image(580, -30, "star.png")
star2.scale_by(0.1)
stars = [star1, star2]
ninja1 = uvage.from_image(100, -30, "baddie.png")
ninja2 = uvage.from_image(300, -30, "baddie.png")
ninja3 = uvage.from_image(485, -30, "baddie.png")
ninja4 = uvage.from_image(700, -30, "baddie.png")
baddies = [ninja1, ninja2, ninja3, ninja4]
for each in baddies:
    each.scale_by(0.2)
heart1 = uvage.from_image(30, 30, "heart.png")
heart1.size = [40, 40]
heart2 = uvage.from_image(70, 30, "heart.png")
heart2.size = [40, 40]
heart3 = uvage.from_image(110, 30, "heart.png")
heart3.size = [40, 40]
bomb1 = uvage.from_image(220, -30, "bomb.png")
bomb1.scale_by(0.25)
bomb2 = uvage.from_image(445, -30, "bomb.png")
bomb2.scale_by(0.25)
bombs = [bomb1, bomb2]
end_text = uvage.from_text(400, 300, "GAME OVER", 50, "red")
restart_instructions = uvage.from_text(400, 340, "press space bar to play again", 40, "red")

def tick():
    global lives_left
    global game_over
    global points
    global clock
    camera.draw(background)
    if not game_over:
        clock += 1
    score = uvage.from_text(750, 30, str(points), 40, "red")
    if clock <= 135:
        falling["ninja1"] = True
    if 90 <= clock:
        falling["star2"] = True
    if 65 <= clock:
        falling["ninja3"] = True
    if 135 <= clock:
        falling["bomb2"] = True
    if 200 <= clock:
        falling["star1"] = True
    if 225 <= clock:
        falling["ninja2"] = True
    if 285 <= clock:
        falling["bomb1"] = True
    if 300 <= clock:
        falling["ninja4"] = True
    if clock >= 430:
        clock = 0
    for ninja in baddies:
        name = "ninja" + str(baddies.index(ninja) + 1)
        if falling[name] and not game_over:
            ninja.y += 3
        if ninja.bottom_touches(sword, 0, -10):
            points += 10
            ninja.y = -30
            falling[name] = False
        if ninja.y >= 580:
            ninja.y = -30
            falling[name] = False
    for star in stars:
        name = "star" + str(stars.index(star) + 1)
        if falling[name] and not game_over:
            star.y += 3
        if star.touches(sword):
            if lives_left < 3:
                lives_left += 1
            star.y = -30
            falling[name] = False
        if star.y >= 590:
            star.y = -30
            falling[name] = False
    for bomb in bombs:
        name = "bomb" + str(bombs.index(bomb) + 1)
        if falling[name] and not game_over:
            bomb.y += 5
        if bomb.touches(sword):
            lives_left -= 1
            bomb.y = -30
            falling[name] = False
        if bomb.y >= 590:
            bomb.y = -30
            falling[name] = False
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
    for ninja in baddies:
        camera.draw(ninja)
    for star in stars:
        camera.draw(star)
    for bomb in bombs:
        camera.draw(bomb)
    if lives_left >= 1:
        camera.draw(heart1)
    if lives_left >= 2:
        camera.draw(heart2)
    if lives_left == 3:
        camera.draw(heart3)
    if lives_left == 0:
        game_over = True
    if game_over:
        camera.draw(end_text)
        camera.draw(restart_instructions)
        if uvage.is_pressing("space"):
            game_over = False
            points = 0
            clock = 0
            lives_left = 3
    camera.draw(score)
    camera.draw(sword)
    camera.display()


uvage.timer_loop(30, tick)
