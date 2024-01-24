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