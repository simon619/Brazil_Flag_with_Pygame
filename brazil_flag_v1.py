import pygame

class BrazilFlag:

    def __init__(self, w, h):
        self.screen_width = w
        self.screen_height = h
        self.window = None
        self.center = (500, 350, 5, 5)
        self.my_font_star = None
        self.my_font_heading = None
        self.my_font_heading = None
        self.white = (255, 255, 255)
        self.green = (0, 151, 57)
        self.yellow = (254, 221, 0)
        self.blue = (1, 33, 105)
        self.light_black = (54, 69, 79)

    def draw_pixels(self, x, y, color):
        pygame.draw.rect(self.window, color, (x, y, 2, 2))
        pygame.display.update()

    def draw_star(self, tup, ch):
        star = self.my_font_star.render(str(ch), True, self.white)
        self.window.blit(star, (tup[0], tup[1]))

    def draw_text(self, tup):
        text = self.my_font_text.render(str(tup[3]), True, self.green)
        text = pygame.transform.rotate(text, tup[2])
        self.window.blit(text, (tup[0], tup[1]))

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
        self.dda_algo_run(200, 140, 800, 140, self.green)
        self.dda_algo_run(200, 140, 200, 560, self.green)
        
        self.dda_algo_run(800, 560, 200, 560, self.green)
        self.dda_algo_run(800, 560, 800, 140, self.green)

        self.dda_algo_run(250, 350, 500, 190, self.yellow)
        self.dda_algo_run(250, 350, 500, 510, self.yellow)

        self.dda_algo_run(750, 350, 500, 190, self.yellow)
        self.dda_algo_run(750, 350, 500, 510, self.yellow) 

    def circle_point(self, p, q, h, k, color):
        self.draw_pixels(h + p, k + q, color)
        self.draw_pixels(h + q, k + p, color)
        self.draw_pixels(h + q, k - p, color)
        self.draw_pixels(h + p, k - q, color)
        self.draw_pixels(h - p, k - q, color)
        self.draw_pixels(h - q, k - p, color)
        self.draw_pixels(h - q, k + p, color)
        self.draw_pixels(h - p, k + q, color)
       
    def midpoint_algo_run(self, rad, h, k, color):
        d = 1 - rad
        x = 0
        y = rad
        self.circle_point(x, y, h, k, color)
        while x < y:
            if d < 0:
                d = d + 2 * x + 3
                x += 1
            else:
                d = d + 2 * x - 2 * y + 5
                x += 1
                y -= 1
            self.circle_point(x, y, h, k, color)
    
    def midpoint_setup(self):
        self.midpoint_algo_run(100, 500, 350, self.blue)

    def arc_point(self, p, q, h, k, color):
        self.draw_pixels(h + p, k - q, color)

    def midpoint_algo_arc_run(self, rad, h, k, color):
        d = 1 - rad
        x = 0
        y = rad
        self.arc_point(x, y, h, k, color)
        while x < y:
            if d < 0:
                d = d + 2 * x + 3
                x += 1
            else:
                d = d + 2 * x - 2 * y + 5
                x += 1
                y -= 1
            self.arc_point(x, y, h, k, color)

    def arc_setup(self):
        self.midpoint_algo_arc_run(253, 417, 550, self.white)
        self.midpoint_algo_arc_run(255, 411, 563, self.white)

    def star_setup(self):
        star_coordinates = [(503, 340), (500, 360), (520, 338), (487, 370), ( 513, 370), 
                            (499, 390), (572, 385), (554, 384), (560, 393), (555, 400), 
                            (548, 403), (539, 402), (539, 412), (539, 422), (529, 404), 
                            (519, 410), (512, 399), (415, 320), (416, 368), (425, 360), 
                            (434, 352), (450, 369), (444, 379), (460, 395), (463, 337), 
                            (535, 305)]
        
        for cor in star_coordinates:
            self.draw_star(cor, '*')
    
    def text_setup(self):
        text_coordinates = [(425, 300, 360, 'O'), (435, 300, 359, 'R'), (445, 301, 359, 'D'),
                            (455, 302, 359, 'E'), (465, 304, 359, 'M'), (485, 310, 357, 'O'),
                            (505, 316, 351, 'P'), (515, 320, 351, 'R'), (525, 325, 351, 'O'), 
                            (535, 331, 340, 'G'), (545, 337, 340, 'R'), (555, 344, 335, 'E'), 
                            (565, 351, 320, 'S'), (575, 359, 320, 'S'), (583, 367, 315, 'O')]
        
        for cor in text_coordinates:
            self.draw_text(cor)

    def heading_setup(self):
        self.draw_heading((240, 80, "MISSION HEXA IS ON"))
        self.draw_heading((260, 580, "LET'S GO, BRAZIL!!!"))
        
    def build_screen(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.window.fill(self.light_black)
        pygame.display.set_caption("Brazil")
        self.my_font_star = pygame.font.Font('freesansbold.ttf', 20)
        self.my_font_text = pygame.font.Font('freesansbold.ttf', 7)
        self.my_font_heading = pygame.font.Font('freesansbold.ttf', 50)

        running = True
        while running:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    self.dda_setup()
                    self.midpoint_setup()
                    self.arc_setup()
                    self.star_setup()
                    self.text_setup()
                    self.heading_setup()
                if keys[pygame.K_SPACE]:
                    self.window.fill(self.light_black)
                if keys[pygame.K_ESCAPE]:
                    running = False
                    pygame.quit()
                    break
                pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    width, height = 1000, 700
    obj = BrazilFlag(width, height)
    obj.build_screen()
