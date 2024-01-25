# 1) Key Stages in a Game Loop

# GAME LOOP - for loop composed of four key stages
# I: Process user input
# II: Update state of game objects, 
# III: Render/draw update game state and create display/audio output
# IV: Control frame rate (speed of loop iteration) of game

# FRAME - each cycle of game loop (occurs multiple times in a second)
# continue until condition to exit game is met

# 2) Creating Sprites with Surfaces and Rectangles

# SURFACE - a canvas where graphics can be drawn
# images can be loaded onto a Surface, or a blank one can be used for drawing

# RECTANGLE - rectangular area defined by its position and size
# used to manage position and dimensions of a Surface

# img_surf = pygame.Surface((width, height))
# img_rect = img_surface.get_rect()

# Game Loop -> Render image
# screen.blit(img_surf, img_rect)

# DRAW - add graphics or shapes directly to a surface
# BLIT - update screen by copying the contents of a img_surface to the
# screen at the specific position of img_rect

# 3) Sprites and Sprite Groups

# SPRITE - 2D image of elements in game environment that can be moved and interacted with
# common attributes include position and speed
# pygame provides a Sprite class that
## create multiple instances
## give access to its built-in methods
## able to extend for new methods

# NOTE: main module/library - pygame, module - sprite, class - Group

# SPRITE GROUPS - pygame.sprite.Group() is useful because:
## container that manages Sprite opjects
## include methods for collision detection
## update position and render multiple sprites easier

# COLLISION DETECTION - checking whether two or more game objects are overlapping

# pygame.sprite.spritecollideany() is a useful method:
## arguments are a Sprite and a Group
## check every object in the Group if its .rect() intersects with the rest of the sprite
## returns True if detected and False otherwise

# IMAGE; pygame.image.load('file_name.png') -  load image and transfer to a Surface
## .convert() optimizes the Surface and making future .blit() calls faster

# 4) User Events and its Applications

# USEREVENT - used to define their own events with custom identifies
## trigger specific actions in response to certain game conditions

# Defining a USEREVENT
# custome_event_1 = pygame.USEREVENT + 1

# pygame.event.get() - returns list of events in the event queue
# pygame.event.get_pressed() - returns dict of event in event queue


