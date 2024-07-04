import pygame,os,time,random,sys

pygame.init()
width = 1200
heigth = 800
fps = 30
spaceship_speed = 20
speed_of_enemy = 4




screen = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("Space-ship")
clock = pygame.time.Clock()
my_font = pygame.font.SysFont("Times New Roman",20)


background  = pygame.image.load("space\\space_invaders_background.gif")

spaceship_image = pygame.image.load("space\\player.png")
background_image = pygame.image.load("space\\m_HkaoI.png")
bullet_image = pygame.image.load("space\\bullet.png")
enemy_image = pygame.image.load("space\\enemy.png")
all_sprites = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player = pygame.sprite.Group()

score = 0


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = spaceship_image
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2,heigth - 50)
        

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += spaceship_speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= spaceship_speed
        if keys[pygame.K_UP]:
            self.rect.y -= spaceship_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += spaceship_speed


        if self.rect.right >= width:
            self.rect.right = width
        
        if self.rect.left <=  0:
            self.rect.left = 0
        
        if self.rect.bottom >= heigth:
            self.rect.bottom = heigth
        
        if self.rect.top <= 300:
            self.rect.top = 300
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        self.rect.y -= 15
        if self.rect.bottom < 0:
            self.kill()
        




class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center  = (width / 2,40)


    def update(self):
        self.rect.y += speed_of_enemy
        if self.rect.top > heigth:
            self.rect.top = 0
            self.rect.centerx = random.randint(0,width)

        if self.rect.bottom >= heigth:
            pygame.quit()
            sys.exit()

            



spaceship = Spaceship()
enemy = Enemy()
second_enemy = Enemy()
second_enemy.rect.topleft = (20,20)
third_enemy = Enemy()
third_enemy.rect.topright = (800,20)
four_enemy = Enemy()
four_enemy.rect.center = (400,20)



all_sprites.add(spaceship)
all_sprites.add(enemy)
all_sprites.add(second_enemy)
all_sprites.add(third_enemy)
all_sprites.add(four_enemy)

enemy_group.add(enemy)
enemy_group.add(second_enemy)
enemy_group.add(third_enemy)
enemy_group.add(four_enemy)
player.add(spaceship)

bullet = Bullet(spaceship.rect.x,spaceship.rect.y)

button_surface = pygame.Surface((150,50))
button_text = my_font.render("Start game",True,(0,0,0))
text_rect = button_text.get_rect(center = (button_surface.get_width() /2,button_surface.get_height()/ 2))
button_rect = pygame.Rect(300,200,400,400)

quit_surface = pygame.Surface((150,50))
quit_text = my_font.render("Quit game",True,(0,0,0))
quit_text_rect = quit_text.get_rect(center = (quit_surface.get_width()  /2,quit_surface.get_height()/ 2))
quit_rect = pygame.Rect(300,600,400,400)
begin = False

while (begin == False):
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            begin = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                begin = True
        
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface,(127,127,212),(1,1,148,48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if quit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    
    
    
    
    if quit_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(quit_surface,(192,192,192),(1,1,148,48))
    else:
        pygame.draw.rect(quit_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(quit_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(quit_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(quit_surface, (0, 100, 0), (1, 48, 148, 10), 2)
    

    button_surface.blit(button_text,text_rect)
    screen.blit(button_surface,(button_rect.x,button_rect.y))
    quit_surface.blit(quit_text,quit_text_rect)
    screen.blit(quit_surface,(quit_rect.x,quit_rect.y))
    pygame.display.flip()
    clock.tick(fps)


paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet(spaceship.rect.x + 50 ,spaceship.rect.y)
            all_sprites.add(bullet)
            bullet_group.add(bullet)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        
    if not paused:
        all_sprites.update()


        #TODO Столкновение пулей с объектами
        for bullet in bullet_group:
            hits = pygame.sprite.spritecollide(bullet,enemy_group,False)
            if hits:
                bullet.kill()
                score += 1
                if score == 100:
                    speed_of_enemy += 3
                for hit in hits:
                    hit.rect.top = 0
                    hit.rect.centerx = random.randint(0,width)

        



        if pygame.sprite.groupcollide(player,enemy_group,True,True):
            time.sleep(0.5)
            running = False

        


        text = my_font.render(f"Score: {score}",True,(255,255,255))
        screen.fill((192,192,192))
        screen.blit(background_image,(0,0))
        screen.blit(text,(10,10))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)

pygame.quit()
