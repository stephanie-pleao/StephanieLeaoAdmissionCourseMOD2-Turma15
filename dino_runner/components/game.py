import pygame

from dino_runner.components.dinossaur import Dinossaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = "freesansbold.ttf"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        self.player = Dinossaur()
        self.obstacle_manager = ObstacleManager()
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.obstacle_manager.update(self)       
        self.player.update(user_input)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #Também aceita código hexadecimal "#FFFFFF"
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect_center = (900, 50)
        self.screen.blit(text, text_rect_center)

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = 260
        half_screen_width = 430

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press any key to start", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect_center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect_center)
        else:
            self.screen.blit(ICON, (half_screen_width + 60, half_screen_height - 40))
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render('Press any key to restart', True, (0, 0, 0))
            score = font.render('Your Score {}'.format(self.score), True, (0, 0, 0))
            death = font.render('Death count: {}'.format(self.death_count), True, (0, 0, 0))
            text_rect_center = (half_screen_width - 20, half_screen_height + 80)
            self.screen.blit(text, text_rect_center)
            score_rect_center = (half_screen_width - 20, half_screen_height + 110)
            self.screen.blit(score, score_rect_center)
            death_rect_center = (half_screen_width - 20, half_screen_height + 140)
            self.screen.blit(death, death_rect_center)
            
        pygame.display.update()
        self.handle_events_on_menu()