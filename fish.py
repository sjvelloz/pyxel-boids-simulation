import pyxel
import math
import random
from constants import WIDTH, HEIGHT, D_BLUE

class Fish:
    def __init__(self):
        # Fish coordinates
        self.x = random.randint(0,WIDTH)
        self.y = random.randint(0,HEIGHT)

        # Fish speed
        self.vx = random.choice([-4, -3, -2, 2, 3, 4])
        self.vy = random.choice([-4, -3, -2, 2, 3, 4])


    def draw(self):
        # ---- Fish sprite -----
        angle = math.atan2(self.vy, self.vx)

        # Fish head
        x1 = self.x + 8 * math.cos(angle)
        y1 = self.y + 8 * math.sin(angle)

        # Fish tail
        x2 = self.x + 5 * math.cos(angle + 2.4)
        y2 = self.y + 5 * math.sin(angle + 2.4)

        x3 = self.x + 5 * math.cos(angle - 2.4)
        y3 = self.y + 5 * math.sin(angle - 2.4)

        pyxel.tri(x1, y1, x2, y2, x3, y3, D_BLUE)

    def update(self):
        # Fish movement
        self.x += self.vx 
        self.y += self.vy

        # Out of bounds behaviour
        if self.x <= 0:
            self.x = WIDTH-1

        if self.x >= WIDTH:
            self.x = 1

        if self.y <= 0:
            self.y = HEIGHT-1

        if self.y >= HEIGHT:
            self.y = 1

        # Speed control
        speed = math.hypot(self.vx, self.vy)
        if 0 < speed < 2.0:
            self.vx = (self.vx/speed) * 2
            self.vy = (self.vy/speed) * 2

        elif speed > 4:
            self.vx = (self.vx/speed) * 4
            self.vy = (self.vy/speed) * 4

    # X-Axis distance between two fishes
    def dx(self, other):
        return math.fabs(self.x-other.x)
    
    # Y-Axis distance between two fishes
    def dy(self, other):
        return math.fabs(self.y-other.y)
    
    # Fish alignment method
    def interact(self, other):
        dist = math.hypot(self.x - other.x, self.y - other.y)

        if dist < 12:
            if self.x < other.x:
                self.vx = -abs(self.vx)
            else:
                self.vx = abs(self.vx)

            if self.y < other.y:
                self.vy = -abs(self.vy)
            else:
                self.vy = abs(self.vy)


        elif dist < 40:
            self.vx += (other.vx - self.vx) * 0.05
            self.vy += (other.vy - self.vy) * 0.05
