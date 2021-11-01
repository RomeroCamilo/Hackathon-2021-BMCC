import pygame
import math
import random
import time

from game import Game

g = Game()

while g.running:
  g.curr_menu.display_menu()
  g.game_loop()


from pygame import mixer

pygame.mixer.pre_init(44100,16,2,4096)

#initialize pygame
pygame.init()

WIDTH, HEIGHT = 640, 360

#create the screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# #background
background = pygame.image.load('./backgroundPygame2.jpg')

# #background music
pygame.mixer.music.load("./cityMusic2.mp3")
pygame.mixer.music.set_volume(3)
pygame.mixer.music.play(-1)


#Title and Icon
pygame.display.set_caption("Salty Platoon")
icon = pygame.image.load('./assets/pixel.png')
pygame.display.set_icon(icon)

# food
avocado_img = pygame.image.load("./assets/avocado.png")
avocado_img = pygame.transform.scale(avocado_img, (25,25))
burger_img = pygame.image.load("./assets/burger.png")
burger_img = pygame.transform.scale(burger_img, (25,25))
diet_img = pygame.image.load("./assets/diet.png")
diet_img = pygame.transform.scale(diet_img, (25,25))
donut_img = pygame.image.load("./assets/donut.png")
donut_img = pygame.transform.scale(donut_img, (25,25))
frenchFry_img = pygame.image.load("./assets/french-fries.png")
frenchFry_img = pygame.transform.scale(frenchFry_img, (25,25))
fruit_img = pygame.image.load("./assets/fruit.png")
fruit_img = pygame.transform.scale(fruit_img, (25,25))
water_img = pygame.image.load("./assets/glass-of-water.png")
water_img = pygame.transform.scale(water_img, (25,25))
pizza_img = pygame.image.load("./assets/pizza.png")
pizza_img = pygame.transform.scale(pizza_img, (25,25))
chicken_img = pygame.image.load("./assets/roasted-chicken.png")
chicken_img = pygame.transform.scale(chicken_img, (25,25))
salad_img = pygame.image.load("./assets/salad.png")
salad_img = pygame.transform.scale(salad_img, (25,25))

#food x values
avocadoX = random.randrange(0, 550)
burgerX = random.randrange(0, 550)
dietX = random.randrange(0, 550)
donutX = random.randrange(0, 550)
frenchFryX = random.randrange(0, 550)
fruitX = random.randrange(0, 550)
waterX = random.randrange(0, 550)
pizzaX = random.randrange(0, 550)
chickenX = random.randrange(0, 550)
saladX = random.randrange(0, 550)

# food y values
avocadoY = 0
avocadoY_change = 0

burgerY = 0
burgerY_change = 0

pizzaY = 0
pizzaY_change = 0

chickenY = 0
chickenY_change = 0

dietY = 0
dietY_change = 0

donutY = 0
donutY_change = 0

frenchFryY = 0
frenchFryY_change = 0

fruitY = 0
fruitY_change = 0

waterY = 0
waterY_change = 0

saladY = 0
saladY_change = 0

foodY = 0
foodY_change = 0


def avocado(x, y):
  WIN.blit(avocado_img, (x, y))

def burger(x, y):
  WIN.blit(burger_img, (x, y))

def diet(x, y):
  WIN.blit(diet_img, (x, y))

def donut(x, y):
  WIN.blit(donut_img, (x, y))

def frenchfry(x, y):
  WIN.blit(frenchFry_img, (x, y))

def fruit(x, y):
  WIN.blit(fruit_img, (x, y))

def water(x, y):
  WIN.blit(water_img, (x, y))

def pizza(x, y):
  WIN.blit(pizza_img, (x, y))

def chicken(x, y):
  WIN.blit(chicken_img, (x, y))

def salad(x, y):
  WIN.blit(salad_img, (x, y))


# end of food functions

# score and health points
score = 0
health_points = 100
font = pygame.font.Font('freesansbold.ttf', 32)

scoreX = 10
scoreY = 10
health_pointsX = 450
health_pointsY = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_health_points(x, y):
  health_val = font.render("Health: " + str(health_points),True, (255, 255, 255))
  WIN.blit(health_val, (x, y))


def show_score(x, y):
  score_val = font.render("Score: " + str(score),True, (255, 255, 255))
  WIN.blit(score_val, (x, y))

# game over function
def game_over_text(x, y):
  game_over_val = game_over_font.render("GAME OVER ",True, (255, 255, 255))
  WIN.blit(game_over_val, (x, y))

# collision function
def isCollision(foodx, foody, playerx, playery):

  distance = math.sqrt((math.pow(foodx - playerx, 2)) + (math.pow(foody - playery, 2)))
  if distance < 45:
    return True
  else:
    return False


# Player
player_img = pygame.image.load("./assets/man.png")
player_img = pygame.transform.scale(player_img, (100, 100))
playerX = 320
playerY = 180
playerX_change = 0
playerY_change = 0


dead = False
def countdown(t, x, y):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    countdown_val = game_over_font.render(str(timer), True, (255, 255, 255))
    WIN.blit(countdown_val, (x, y))
    # print(timer, end="\r")
    time.sleep(1)
    t -= 1

t = 5

def player(x,y):
  WIN.blit(player_img, (x, y))

#while running is true, the screen will be open
running = True


while running:
  WIN.fill((0, 0, 0))
  WIN.blit(background, (0,0))

  for event in pygame.event.get():
    #WILL check if we quit the game or not. If we quit, the screen will close.
    if event.type == pygame.QUIT:
      running = False
    #keypress funcionality for player
    if event.type == pygame.KEYDOWN:
      print("A key has been pressed")
      if event.key == pygame.K_LEFT:
        playerX_change -= 1
        print("Left arrow is pressed")
      elif event.key == pygame.K_RIGHT:
        playerX_change += 1
        print("Right arrow is pressed")
      elif event.key == pygame.K_UP:
        playerY_change -= 1
        print("Up arrow is pressed")
      elif event.key == pygame.K_DOWN:
        playerY_change += 1
        print("Down arrow is pressed")
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        playerX_change = 0
        playerY_change = 0
        print("Keystroke has been released")




  playerX += playerX_change
  playerY += playerY_change
  # addind boarders
  if playerX <= 0:
    playerX = 0
  elif playerX >= 550:
    playerX = 550

  if playerY >= 260:
    playerY = 260
  elif playerY <= 100:
    playerY = 100

  # food movementment

  avocadoY += avocadoY_change
  if avocadoY <= 0:
    avocadoY_change += 1
  elif avocadoY >= 360:
    avocadoX = random.randrange(0, 550)
    avocadoY = 0

  burgerY += burgerY_change
  if burgerY <= 0:
    burgerY_change += 1
  elif burgerY >= 360:
    burgerX = random.randrange(0, 550)
    burgerY = 0

  pizzaY += pizzaY_change
  if pizzaY <= 0:
    pizzaY_change += 1
  elif pizzaY >= 360:
    pizzaX = random.randrange(0, 550)
    pizzaY = 0

  chickenY += chickenY_change
  if chickenY <= 0:
    chickenY_change += 1
  elif chickenY >= 360:
    chickenX = random.randrange(0, 550)
    chickenY = 0

  dietY += dietY_change
  if dietY <= 0:
    dietY_change += 1
  elif dietY >= 360:
    dietX = random.randrange(0, 550)
    dietY = 0

  donutY += donutY_change
  if donutY <= 0:
    donutY_change += 1
  elif donutY >= 360:
    donutX = random.randrange(0, 550)
    donutY = 0

  frenchFryY += frenchFryY_change
  if frenchFryY <= 0:
    frenchFryY_change += 1
  elif frenchFryY >= 360:
    frenchFryX = random.randrange(0, 550)
    frenchFryY = 0

  fruitY += fruitY_change
  if fruitY <= 0:
    fruitY_change += 1
  elif fruitY >= 360:
    fruitX = random.randrange(0, 550)
    fruitY = 0

  waterY += waterY_change
  if waterY <= 0:
    waterY_change += 1
  elif waterY >= 360:
    waterX = random.randrange(0, 550)
    waterY = 0

  saladY += saladY_change
  if saladY <= 0:
    saladY_change += 1
  elif saladY >= 360:
    saladX = random.randrange(0, 550)
    saladY = 0

  # food collision
  avoCollision = isCollision(avocadoX, avocadoY, playerX, playerY)
  if avoCollision:
    score += 1
    health_points += 1
    avocadoX = random.randrange(0, 550)
    avocadoY = 0
    print(score)

  burgerCollision = isCollision(burgerX, burgerY, playerX, playerY)
  if burgerCollision:
    health_points -= 10
    burgerX = random.randrange(0, 550)
    burgerY = 0
    print(score)

  pizzaCollision = isCollision(pizzaX, pizzaY, playerX, playerY)
  if pizzaCollision:
    health_points -= 10
    pizzaX = random.randrange(0, 550)
    pizzaY = 0
    print(score)

  chickenCollision = isCollision(chickenX, chickenY, playerX, playerY)
  if chickenCollision:
    score += 1
    health_points += 1
    chickenX = random.randrange(0, 550)
    chickenY = 0
    print(score)

  dietCollision = isCollision(dietX, dietY, playerX, playerY)
  if dietCollision:
    score += 1
    health_points += 1
    dietX = random.randrange(0, 550)
    dietY = 0
    print(score)

  donutCollision = isCollision(donutX, donutY, playerX, playerY)
  if donutCollision:
    health_points -= 10
    donutX = random.randrange(0, 550)
    donutY = 0
    print(score)

  frenchFryCollision = isCollision(frenchFryX, frenchFryY, playerX, playerY)
  if frenchFryCollision:
    health_points -= 10
    frenchFryX = random.randrange(0, 550)
    frenchFryY = 0
    print(score)

  fruitCollision = isCollision(fruitX, fruitY, playerX, playerY)
  if fruitCollision:
    score += 1
    health_points += 1
    fruitX = random.randrange(0, 550)
    fruitY = 0
    print(score)

  waterCollision = isCollision(waterX, waterY, playerX, playerY)
  if waterCollision:
    score += 1
    health_points += 10
    waterX = random.randrange(0, 550)
    waterY = 0
    print(score)

  saladCollision = isCollision(saladX, saladY, playerX, playerY)
  if saladCollision:
    score += 1
    health_points += 1
    saladX = random.randrange(0, 550)
    saladY = 0
    print(score)

  # health cap
  if health_points >= 100:
    health_points = 100
  # game over
  if health_points <= 0:
    health_points = 0
    game_over_text(100, 300)
    # countdown(t, 250, 100)
    # if t == 0:
    #   dead = True
    #
    # if dead == True:
    #   break




  player(playerX, playerY)
  show_health_points(health_pointsX, health_pointsY)
  show_score(scoreX, scoreY)
  avocado(avocadoX, avocadoY)
  burger(burgerX, burgerY)
  pizza(pizzaX, pizzaY)
  chicken(chickenX, chickenY)
  diet(dietX, dietY)
  donut(donutX, donutY)
  frenchfry(frenchFryX, frenchFryY)
  fruit(fruitX, fruitY)
  water(waterX,waterY)
  salad(waterX, waterY)
  pygame.display.update()

# end of while loop
