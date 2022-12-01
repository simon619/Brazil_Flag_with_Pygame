import pygame

class ArgentinaFlag:

    def __init__(self, w, h):
        self.screen_width = w
        self.screen_height = h
        self.center = (500, 350)
        self.my_font_heading = None
        self.white = (255, 255, 255)
        self.sky_blue = (135, 206, 235)
        self.image = None

    def draw_pixels(self, x, y, color):
        pygame.draw.rect(self.window, color, (x, y, 2, 2))
        pygame.display.update()

    def draw_heading(self, tup):
        text = self.my_font_heading.render(str(tup[2]), True, self.white)
        self.window.blit(text, (tup[0], tup[1]))

    def dda_algo_run(self, x0, y0, x1, y1, color):
        dx = x1 - x0
        dy = y1 - y0
        steps = 0
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)

        (x_inc, y_inc) = (dx / steps, dy / steps)

        for i in range(0, steps):
            self.draw_pixels(x0, y0, color)
            x0 = x0 + x_inc
            y0 = y0 + y_inc

    def dda_setup(self):
        self.dda_algo_run(200, 140, 800, 140, self.sky_blue)
        self.dda_algo_run(200, 140, 200, 280, self.sky_blue)
        self.dda_algo_run(200, 420, 200, 560, self.sky_blue)

        self.dda_algo_run(800, 560, 200, 560, self.sky_blue)
        self.dda_algo_run(800, 560, 800, 420, self.sky_blue)
        self.dda_algo_run(800, 280, 800, 140, self.sky_blue)

        self.dda_algo_run(200, 280, 200, 420, self.white)
        self.dda_algo_run(800, 420, 800, 280, self.white)

        self.dda_algo_run(200, 280, 800, 280, self.white)
        self.dda_algo_run(200, 420, 800, 420, self.white)
        
        for i in range(140, 560):
            if 280 <= i <= 420:
                self.dda_algo_run(200, i, 800, i, self.white)
            else:
                self.dda_algo_run(200, i, 800, i, self.sky_blue)

    def add_center_sun(self):
        self.window.blit(self.image, (446, 296))

    def heading_setup(self):
        self.draw_heading((270, 580, "VAMOS ARGENTINA"))

    def build_screen(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        # self.window.fill(self.light_black)
        pygame.display.set_caption("Argentina")
        load_image = pygame.image.load("center_sun.png")
        self.image = pygame.transform.scale(load_image, (110, 110))
        self.my_font_heading = pygame.font.Font('freesansbold.ttf', 50)
        start_text = self.my_font_heading.render("Press \"Enter\" to Start", True, self.white)
        self.window.blit(start_text, (250, 350))

        running = True
        while running:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    self.window.fill((0, 0, 0))
                    self.dda_setup()
                    self.add_center_sun()
                    self.heading_setup()
                if keys[pygame.K_SPACE]:
                    self.window.fill((0, 0, 0))
                if keys[pygame.K_ESCAPE]:
                    running = False
                    pygame.quit()
                    break
                pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    width, height = 1000, 700
    obj = ArgentinaFlag(width, height)
    obj.build_screen()
