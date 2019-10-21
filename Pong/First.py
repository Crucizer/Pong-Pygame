#Importing Moudules
import pygame as pg
import time
#Intialize Pygame
pg.init()
# TO Make The Screen Stuff
display_width = 1000
display_height = 600
dp = pg.display.set_mode((display_width, display_height))
# Setting Caption
pg.display.set_caption('Pong')
# Paddle1 Stuff
x = 990
y = 300
# Paddle2 Stuff
x_2 = 0
y_2 = 300
v = 8
# Color Variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (210, 0, 0)
green = (0, 210, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
#Animation
FPS = 60
sp = pg.time.Clock()
#Paddle Variables
paddle_width = 10
paddle_height = 100
# Ball Variables
clock = pg.time.Clock()
ball_size = 10
ball_speedx = 6
ball_speedy = 6
pos_x = 300
pos_y = 450
a = True
ball_radius = 5
#Score Variables
player2 = 0
player1 = 0
#Music Bitches
pg.mixer.music.load("soundtrack.mp3")
beep = pg.mixer.Sound("beep.wav")
#Game Over
gameover = None

# They Draw The Paddles And Middle Line
def drawpaddles():
    global paddle1
    global paddle2
    paddle1 = pg.draw.rect(dp, white, (x, y, paddle_width, paddle_height))
    paddle2 = pg.draw.rect(dp, white, (x_2, y_2, paddle_width, paddle_height))
    pg.draw.rect(dp, white, (display_width / 2, 0, 1, display_height))
# This moves the paddle 1
def movepaddle1():
    global y
    y_c = 0
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and y > v:
        y_c -= v
    if keys[pg.K_DOWN] and y < display_height - 100:
        y_c += v
    y += y_c
    # This moves the paddle2
def movepaddle2():
    global y_2
    y_c2 = 0
    key = pg.key.get_pressed()
    if key[pg.K_a] and y_2 > v:
        y_c2 -= v
    if key[pg.K_z] and y_2 < display_height - 100:
        y_c2 += v
    y_2 += y_c2
# This draws the ball
def drawball():
    global ball
    ball = pg.draw.circle(dp, (255, 0, 0), (pos_x, pos_y), ball_size, ball_size)
#This moves the fuckin ball
def movetheball():
    global pos_x
    global pos_y
    global ball_speedx
    global ball_speedy
    pos_x += ball_speedx
    pos_y += ball_speedy
    if pos_y + ball_size > display_height or pos_y - ball_size < 0:
        ball_speedy *= -1
#This Function Checks For The Collison Between Ball And Paddle, and If There is Not A Collison Between
#Ball And Paddle, It Resets The Ball To The Centre(For Both Paddles)
def collison():
#For The Second Paddle
    global pos_y
    global pos_x
    global ball_speedx
    global ball_speedy
    global player2
    global player1
    if pos_x + ball_radius > x:
        if y - 5 < pos_y + ball_radius < y + paddle_height + 5:
            ball_speedx = -ball_speedx
            pg.mixer.Sound.play(beep)

        else:
            pos_x = int(display_width / 2)
            pos_y = int(display_height / 2)
            player2 += 1
            ball_speedx = -6
            ball_speedy = -6
#For The First Paddle
    elif pos_x + ball_radius < 15:
        if y_2 - 5< pos_y + ball_radius < y_2 + paddle_height +5:
            ball_speedx = -ball_speedx
            pg.mixer.Sound.play(beep)
            ball_speedx += 2
            ball_speedy += 2
        else:
            player1 += 1
            pos_x = int(display_width / 2)
            pos_y = int(display_height / 2)
            ball_speedx = 6
            ball_speedy = 6
# More Variables For ScoreBoard
font = pg.font.Font(None, 40)
#This Display The Score And The "Light" And "L" Thing
def score():
    text2 = str(player1)
    text = str(player2)
    light = "Light"
    L = "L"
    p1_score_render = font.render(text, 1, white)
    dp.blit(p1_score_render, (300, 50))
    p2_score_render = font.render(text2, 1, white)
    dp.blit(p2_score_render, (display_width - 300, 50))
    light_render  = font.render(light, 1, white)
    l_render = font.render(L, 1, white)
    dp.blit(light_render, (display_width/2 - 100, 50))
    dp.blit(l_render, (int(display_width/2 + 40), 50))
#More Music Variables
time.sleep(1)
pg.mixer.music.play(-1)


#The Ending Message Function
#Which Quite Doesn't Work Now
font1 = pg.font.Font(None, 210)
def end_message():
    global gameover
    if player2 == 10:
        msg = "Player 2 Lose"#"Player 2 Lose,Press A To Play Again Or Q To Exit"
        msg_render = font1.render(msg, 1, white)
        dp.blit(msg_render, (10, 200))
        gameover = True
        print('Player 2 Lose')
        pg.quit()
        quit()
        # time.sleep(20)
    if player1 == 10:
        msg1 = "Player 1 Lose"#"Player 1 Lose,Press A To Play Again Or Q To Exit"
        msg_render1 = font1.render(msg1, 1, white)
        dp.blit(msg_render1, (10, 200))
        gameover = True
        print('Player 1 Lose')
        pg.quit()
        quit()
        #time.sleep(20)
def game_intro():
    x = True
    clocky = pg.time.Clock()
    while x:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        image = pg.image.load('image.jpg')
        dp.blit(image, (0, 0))
        fonty = pg.font.Font(None, 210)
        texty = "TENNIS"
        texty_render = fonty.render(texty, 1, white)
        dp.blit(texty_render, (300, 50))
        #For Image


        #More Variables For Intro Boxes

        posx_intro1_2 = int(display_width / 2) - 95
        posy_intro1 = int(display_height / 2 - 65)
        posy_intro2 = int(display_height / 2 + 30)
        rect_width = 200
        rect_height = 60
        action = None

        #Button1
        click = pg.mouse.get_pressed()
        mouse = pg.mouse.get_pos()
        if posx_intro1_2 + rect_width > mouse[0] > posx_intro1_2:
            if posy_intro1 + rect_height > mouse[1] > posy_intro1:
                pg.draw.rect(dp, green, (posx_intro1_2, posy_intro1, rect_width, rect_height))
                if click[0] == 1:
                    action = "play"
            else:
                pg.draw.rect(dp, bright_green, (posx_intro1_2, posy_intro1, rect_width, rect_height))
        MediumFont = pg.font.Font(None, 53)
        texti = "MultiPlayer"
        texti_render = MediumFont.render(texti, 1, black)
        dp.blit(texti_render, (int(display_width / 2) - 96, int(display_height / 2 - 55)))


        #Button2


        if posx_intro1_2 + rect_width > mouse[0] > posx_intro1_2:
            if posy_intro2 + rect_height > mouse[1] > posy_intro2:
                pg.draw.rect(dp, red, (posx_intro1_2, posy_intro2, rect_width, rect_height))
                if click[0] == 1:
                    action = "quit"
            else:
                pg.draw.rect(dp, bright_red, (posx_intro1_2, posy_intro2, rect_width, rect_height))
        MediumFont1 = pg.font.Font(None, 63)
        texti1 = "Quit"
        texti_render1 = MediumFont1.render(texti1, 1, black)
        dp.blit(texti_render1, (int(display_width / 2) - 56, int(display_height / 2 +38)))

        if action == "play":
            game_loop()
        if action == "quit":
            pg.quit()
            quit()

        pg.display.update()
        clocky.tick(60)

def game_loop():
    global a
    while a:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        # while gameover == True:
        #     dp.fill(black)
        #     pg.display.update()
        #
        #     for event in pg.event.get():
        #         if event.type == pg.KEYDOWN:
        #             if event.key == pg.K_a:
        #                 game_loop()
        #             if event.key == pg.K_q:
        #                 pg.quit()
        #                 quit()
        dp.fill(black)
        drawpaddles()
        drawball()
        movetheball()
        movepaddle1()
        movepaddle2()
        score()
        collison()
        end_message()
        sp.tick(FPS)
        pg.display.update()
game_intro()
game_loop()
pg.quit()
