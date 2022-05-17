import pygame, sys
import random

class Player:
    def __init__(self, width, height, player_x, player_y):
        self.player = pygame.Rect(player_x, player_y, width, height)

    def drawrect(self, color):
        pygame.draw.rect(screen, (color), self.player)
    
    def update(self,key_1, key_2):
        self.userInput = pygame.key.get_pressed()

        if self.userInput[key_1]:
            self.player.y += 15
        if self.userInput[key_2]:
            self.player.y -= 15
    
    def bound(self):
        if self.player.y >= 530:
            self.player.y = 530
        elif self.player.y <= 0:
            self.player.y = 0

class Ball:
    def __init__(self, width, height, ball_x, ball_y):
        self.ball = pygame.image.load("/home/aadigodzilla/Documents/Projects/Python Projects/Pong Game/res/textures/ball.png")
        self.ball = pygame.transform.scale(self.ball, (width, height))
        self.ball_rect = self.ball.get_rect()
        self.ball_rect.center = (ball_x, ball_y)
        self.speed_x = 6
        self.speed_y = 6
    
    def drawball(self):
        screen.blit(self.ball, self.ball_rect)
    
    def update(self):
        self.ball_rect.x += self.speed_x
        self.ball_rect.y += self.speed_y

        if self.ball_rect.y >= 588:
            pygame.mixer.Sound.play(sound_wall)
            self.speed_y = -self.speed_y
        elif self.ball_rect.y <= 0:
            pygame.mixer.Sound.play(sound_wall)
            self.speed_y = -self.speed_y

class MidLine:
    def __init__(self, width, height, line_x, line_y):
        self.line = pygame.Rect(line_x, line_y, width, height)
        self.line.center = (line_x, line_y)
    
    def drawline(self, color):
        pygame.draw.rect(screen, (color), self.line)

def pause():
    global paused

    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False    

        pause_font = font.render("PAUSED", True, (255,255,255))
        pause_subfont = subfont.render("Press ESCAPE to continue", True, (255,255,255))
        pause_subrect = pause_subfont.get_rect()
        pause_subrect.center = (400,500)
        pause_rect = pause_font.get_rect()
        pause_rect.center = (400,300)
        screen.blit(pause_font, pause_rect)
        screen.blit(pause_subfont, pause_subrect)

        pygame.display.update()

def timer():
    global start, timeout

    while timeout:

            start -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            if start <= 3000 and start > 2000:
                ball.ball_rect.center = (400,random_num)
                num_3 = font.render("3", False, (255,255,255))
                num_3_rect = num_3.get_rect(center=(400, 100))
                screen.blit(num_3, num_3_rect)

            if start <= 2000 and start > 1000:
                num_3_remover = font.render("3", False, (0,0,0))
                num_3_remover_rect = num_3_remover.get_rect(center=(400, 100))
                screen.blit(num_3_remover, num_3_remover_rect)

                num_2 = font.render("2", False, (255,255,255))
                num_2_rect = num_2.get_rect(center=(400, 100))
                screen.blit(num_2, num_2_rect)

            if start <= 1000 and start > 0:
                num_2_remover = font.render("2", False, (0,0,0))
                num_2_remover_rect = num_2_remover.get_rect(center=(400, 100))
                screen.blit(num_2_remover, num_2_remover_rect)
            
                num_1 = font.render("1", False, (255,255,255))
                num_1_rect = num_1.get_rect(center=(400, 100))
                screen.blit(num_1, num_1_rect)
        
            if start <= 0:
                timeout = False
        
            pygame.display.update()

def collision():
    global sound_paddle

    if ball.ball_rect.colliderect(player_1.player) or ball.ball_rect.colliderect(player_2.player):
        pygame.mixer.Sound.play(sound_paddle)
        ball.speed_x = -ball.speed_x
        ball.speed_x *= 1.1
        ball.speed_y *= 1.1  

def score_render():
    score_a_render = font.render(str(score_a), True, (255,255,255))
    score_b_render = font.render(str(score_b), True, (255,255,255))
    score_a_rect = score_a_render.get_rect()
    score_b_rect = score_b_render.get_rect()
    score_a_rect.center = (200,50)
    score_b_rect.center = (600,50)
    screen.blit(score_a_render, score_a_rect)
    screen.blit(score_b_render, score_b_rect)

def reset():
    global start, score_a, score_b, timeout, sound_score

    if ball.ball_rect.x > 788:
        pygame.mixer.Sound.play(sound_score)
        timeout = True
        score_a += 1
        start = 3000
        ball.ball_rect.center = (400+6,random_num)
        ball.speed_x = -6
        ball.speed_y = -6

    elif ball.ball_rect.x < 0:
        pygame.mixer.Sound.play(sound_score)
        timeout = True
        score_b += 1
        start = 3000
        ball.ball_rect.center = (400-6, random_num)
        ball.speed_x = 6
        ball.speed_y = 6
            
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

screen_width = 800
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player_1 = Player(10,70,0,0)
player_2 = Player(10,70,790,0)
ball = Ball(12,12,400-6,300)
line = MidLine(1,600,400,300)

font = pygame.font.Font(None, 64)
subfont = pygame.font.Font(None, 32)
score_a = 0
score_b = 0
random_num = random.randrange(50,250)

sound_score = pygame.mixer.Sound("/home/aadigodzilla/Documents/Projects/Python Projects/Pong Game/res/audio/Pong Sound Score.mp3")
sound_paddle = pygame.mixer.Sound("/home/aadigodzilla/Documents/Projects/Python Projects/Pong Game/res/audio/Pong Sound Paddle.mp3")
sound_wall = pygame.mixer.Sound("/home/aadigodzilla/Documents/Projects/Python Projects/Pong Game/res/audio/Pong Sound Wall.mp3")

timeout = True
start = 3000
paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = True

    
    sound_paddle.set_volume(0.4)
    sound_score.set_volume(0.4)
    sound_wall.set_volume(0.4)
    pygame.display.set_caption("Pong Game")
    pygame.display.set_icon(pygame.image.load("/home/aadigodzilla/Documents/Projects/Python Projects/Pong Game/res/textures/ping-pong.png"))

    player_1.update(pygame.K_s, pygame.K_w)
    player_2.update(pygame.K_DOWN, pygame.K_UP)
    ball.update()

    player_1.bound()
    player_2.bound()

    screen.fill((0,0,0))

    player_1.drawrect((255,255,255))
    player_2.drawrect((255,255,255))
    ball.drawball()
    line.drawline((255,255,255))

    score_render()
    pause()
    timer()    
    reset()
    collision()   
    
    clock.tick(60)
    pygame.display.update()