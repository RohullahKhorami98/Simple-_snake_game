import pygame
import time
import random
import sys
class snake:
    def __init__(self,snake_speed, width, height):    
        self.snake_speed = snake_speed
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.screen_width , self.screen_height = width,height
        pygame.init()
        pygame.display.set_caption("Snake 🥛🐍")
        self.snake_window = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.fps = pygame.time.Clock()
        self.snake_defult_position = [100,70]
        self.snake_defult_body = [[200,100],[190,90],[180,80],[170,70]]
        self.target_random_position = [random.randrange(1,(self.screen_width//10))*10,random.randrange(1,(self.screen_height//10))*10]
        self.target_spawn = True
        self.defult_start = "RIGHT"
        self.snake_direction = self.defult_start
        self.score = 0
        self.font = "arial"
        self.fontsize = 40
    def get_score(self,color):
        score_font = pygame.font.SysFont(self.font, self.fontsize)
        display_score = score_font.render("Score : "+ str(self.score), True, color)
        shape_score = display_score.get_rect()
        self.snake_window.blit(display_score,shape_score)
    def game_over(self):
        over_score = pygame.font.SysFont(self.font,self.fontsize)
        game_over_display = over_score.render("Your score is: " + str(self.score), True, self.red)
        game_over_shape = game_over_display.get_rect()
        self.snake_window.blit(game_over_display,game_over_shape)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        quit()
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake_direction = "UP"
                    if event.key == pygame.K_DOWN:
                        self.snake_direction = "DOWN"
                    if event.key == pygame.K_LEFT:
                        self.snake_direction = "LEFT"
                    if event.key == pygame.K_RIGHT:
                        self.snake_direction = "RIGHT"
            if self.snake_direction == "UP" and  self.defult_start !="DOWN":
                self.defult_start = "UP"
            if self.snake_direction == "DOWN" and self.defult_start !="UP":
                self.defult_start = "DOWN"
            if self.snake_direction == "LEFT" and self.defult_start !="RIGHT":
                self.defult_start = "LEFT"
            if self.snake_direction == "RIGHT" and self.defult_start !="LEFT":
                self.defult_start = "RIGHT"
            
            if self.defult_start == "UP":
                self.snake_defult_position[1]-=10
            if self.defult_start == "DOWN":
                self.snake_defult_position[1]+=10
            if self.defult_start == "LEFT":
                self.snake_defult_position[0]-=10
            if self.defult_start == "RIGHT":
                self.snake_defult_position[0]+=10
            
            self.snake_defult_body.insert(0, list(self.snake_defult_position))
            if self.snake_defult_position[0] == self.target_random_position[0] and self.snake_defult_position[1] == self.target_random_position[1]:
                self.score+=10
                self.target_spawn = False
            else:
                self.snake_defult_body.pop()
            if not self.target_spawn:
                self.target_random_position = [random.randrange(1,(self.screen_width//10))*10,random.randrange(1,(self.screen_height//10))*10]
            self.target_spawn = True
            self.snake_window.fill(self.black)

            for i in self.snake_defult_body:
                pygame.draw.rect(self.snake_window, self.green, pygame.Rect(i[0],i[1],20,10))
            pygame.draw.rect(self.snake_window,self.white,pygame.Rect(self.target_random_position[0],self.target_random_position[1],20,10))

            if self.snake_defult_position[0]< 0 or self.snake_defult_position[0]> self.screen_width-10:
                self.game_over()
            if self.snake_defult_position[1]<0 or self.snake_defult_position[1] >self.screen_height-10:
                self.game_over()
            
            for j in self.snake_defult_body[1:]:
                if self.snake_defult_position[0] == j[0] and self.snake_defult_position[1] == j[1]:
                    self.game_over()
            self.get_score(self.blue)
            pygame.display.update()
            self.fps.tick(self.snake_speed)

if __name__== "__main__":
    snake_obj = snake(snake_speed=20, width=850,height=850)
    snake_obj.main()