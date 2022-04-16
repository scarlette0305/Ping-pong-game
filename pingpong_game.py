from pygame import *


#region variables
_WIDTH = 800
_HEIGHT = 640
window = display.set_mode((_WIDTH,_HEIGHT))
clock = time.Clock()
#endregion

class GameSprite(sprite.Sprite):
    def __init__(self, filename, x,y, width, height,speed=0):
        super().__init__()
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (width,height))
        self.rect = Rect(x,y,width,height)
        self.speed = speed
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed

class RectSprite(sprite.Sprite):
    def __init__(self, color, x,y, width, height,speed=0):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = Rect(x,y,width,height)
        self.speed = speed
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(RectSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_j]:
            self.rect.y -= self.speed
        if keys[K_k]:
            self.rect.y += self.speed
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > _HEIGHT - self.rect.height:
            self.rect.y = _HEIGHT - self.rect.height


class Player2(RectSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_f]:
            self.rect.y -= self.speed
        if keys[K_d]:
            self.rect.y += self.speed
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > _HEIGHT  - self.rect.height:
            self.rect.y = _HEIGHT - self.rect.height

ball = Ball("ball.png", 300,300,50,50,5)
bar = Player('blue', _WIDTH-30, 300,30,150,speed=10)
bar2 = Player2('blue', 0, 300,30,150,speed=10)

game_is_running = True
while game_is_running:    
    for e in event.get():
        if e.type == QUIT:
            game_is_running = False
    window.fill((255,255,255))

    bar.update()
    bar.draw(window)
    bar2.update()
    bar2.draw(window)
    ball.update()
    ball.draw(window)

    display.update()
    clock.tick(60)
