## Что такое Sprite


sprite.Group
```python
all_sprites = pygame.sprite.Group()
```


```python
    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
```



### Создание Sprite

```python
class Player(pygame.sprite.Sprite):
```



```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
```


```python
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
```



### Sprite movement

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
```



### Граничные точки

![image](assets/rect_handles.png)


```python
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
```



### Двигаемся к картинкам

![image](assets/p1_jump.png)
![image](assets/p3_walk01.png)


```python
import pygame
import random
import os

# set up asset folders
game_folder = os.path.dirname(__file__)
```


```python
import pygame
import random
import os

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

...

player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()
```


### Используем картинку
```
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
```



### Прозрачность спрайта

```python
# ломаем :)
screen.fill(BLUE)
```


```
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
```
