from pygame import *
from random import randint

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

class RectSprite(sprite.Sprite):
    def __init__(self, filename, x,y, width, height,speed=0):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = Rect(x,y,width,height)
        self.speed = speed
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

game_is_running = True

while game_is_running:
    
    for e in event.get():
        if e.type == QUIT:
            game_is_running = False