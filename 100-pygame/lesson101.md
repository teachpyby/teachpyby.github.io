## Что такое Pygame

Набор модулей (библиотек) для создания игр

 * Graphics and animation
 * Sound (including music)
 * Control (keyboard, mouse, gamepad, etc.)



### Game Loop

 - Process Input (or Events)
 - Update Game
 - Render (or Draw)
 - Clock



### Pygame Template

```python
# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 360  # width of our game window
HEIGHT = 480 # height of our game window
FPS = 30 # frames per second
```


```python
# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
```


```python
# Game Loop
running = True
while running:
    # Process input (events)
    # Update
    # Render (draw)
```



## RGB colors

![image](https://upload.wikimedia.org/wikipedia/commons/c/c2/AdditiveColor.svg)


![image](http://kidscancode.org/blog/img/rgb_color_example.png)


## Общее количество цветов

```python
256 * 256 * 256 = 16,777,216
```



# Render / Draw Section

```
# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
```


```python
    # Draw / render
    screen.fill(BLACK)
```


## double-buffering

![image](https://i.imgur.com/euF6cmD.png)


![image](http://optimum2.mii.lt/JavaTutorial/figures/extra/fullscreen/pageFlipping.gif)


```python
    # Draw / render
    screen.fill(BLACK)
    # *after* drawing everything, flip the display
    pygame.display.flip()
```



### Input / Events Section

```python
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
```



### Controlling FPS

```python
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
```



```python
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw / render
    screen.fill(BLACK)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
```
