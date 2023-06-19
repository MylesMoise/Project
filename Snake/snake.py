import pygame, sys, random
from pygame.math import Vector2
import pathlib

class SNAKE:
    def __init__(self):
        self.body = [Vector2(6,10), Vector2(5,10), Vector2(4,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        self.head = self.body[0]

        #Importing files zzz
        head_down_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/head_down.png'
        head_left_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/head_left.png'
        head_right_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/head_right.png'
        head_up_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/head_up.png'
        body_bl_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/body_bl.png'
        body_br_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/body_br.png'
        body_horizontal_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/body_horizontal.png'
        body_tl_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/body_tl.png'
        body_tr_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/body_tr.png'
        body_vertical_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/body_vertical.png'
        tail_down_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/tail_down.png'
        tail_left_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/tail_left.png'
        tail_right_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/tail_right.png'
        tail_up_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/tail_up.png'
        sound_Path = pathlib.Path(__file__).resolve().parent / 'Sound/crunch.wav'

        self.head_up = pygame.image.load(head_up_Path).convert_alpha()
        self.head_down = pygame.image.load(head_down_Path).convert_alpha()
        self.head_left = pygame.image.load(head_left_Path).convert_alpha()
        self.head_right = pygame.image.load(head_right_Path).convert_alpha()

        self.tail_up = pygame.image.load(tail_up_Path).convert_alpha()
        self.tail_down = pygame.image.load(tail_down_Path).convert_alpha()
        self.tail_right = pygame.image.load(tail_right_Path).convert_alpha()
        self.tail_left = pygame.image.load(tail_left_Path).convert_alpha()

        self.body_vertical = pygame.image.load(body_vertical_Path).convert_alpha()
        self.body_horizontal = pygame.image.load(body_horizontal_Path).convert_alpha()

        self.body_tr = pygame.image.load(body_tr_Path).convert_alpha()
        self.body_tl = pygame.image.load(body_tl_Path).convert_alpha()
        self.body_br = pygame.image.load(body_br_Path).convert_alpha()
        self.body_bl = pygame.image.load(body_bl_Path).convert_alpha()

        self.crunch_sound = pygame.mixer.Sound(sound_Path)

    def draw_snake(self):
        self.head = self.head_right
        self.tail = self.tail_left
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            #Need a rect for position
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            #Figure direction of where snake is looking
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                #Comparing blocks to determine if horizontal or vertical body
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                if previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    #Corner blocks
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        #Create a vector which gives us the movement
        head_compare = self.body[1] - self.body[0]
        if head_compare == Vector2(1,0): self.head = self.head_left
        elif head_compare == Vector2(-1,0): self.head = self.head_right
        elif head_compare == Vector2(0,1): self.head = self.head_up
        elif head_compare == Vector2(0,-1): self.head = self.head_down
        
    def update_tail_graphics(self):
        #Create a vector which gives us the movement
        tail_compare = self.body[-2] - self.body[-1]
        if tail_compare == Vector2(1,0): self.tail = self.tail_left
        elif tail_compare == Vector2(-1,0): self.tail = self.tail_right
        elif tail_compare == Vector2(0,1): self.tail = self.tail_up
        elif tail_compare == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            #Same as else but not removing the "tail"
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:   
            #Make a copy of the body besides the "tail"
            body_copy = self.body[:-1]
            #Put the "head" where the player input is directing it towards
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(6,10), Vector2(5,10), Vector2(4,10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        #create an x and y pos for fruit
        self.randomize()

    def draw_fruit(self):
        #Create a rectangle
        fruit_rect = pygame.Rect((int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size))

        #Draw the fruit
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        #Creating everything in here
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        #Updating the snake and points
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        #Draw items
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #Reposition fruit
            self.fruit.randomize()
            #Add a block to body
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        #Check if snake is outside the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        #Check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        #Creating score
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 60)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#Creating screen and dimensions
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

#Importing files 
apple_Path = pathlib.Path(__file__).resolve().parent / 'Graphics/apple.png'
apple = pygame.image.load(apple_Path).convert_alpha()
font_Path = pathlib.Path(__file__).resolve().parent / 'Font/PoetsenOne-Regular.ttf'
game_font = pygame.font.Font(font_Path, 25)

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            #Create movement
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)