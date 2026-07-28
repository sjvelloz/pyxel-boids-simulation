import pyxel
from fish import Fish
from constants import WIDTH, HEIGHT, L_BLUE, FISHES

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Aquarium")

        # N-fish list
        self.fishes = [Fish() for _ in range(FISHES)]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for fish in self.fishes:
            fish.update()

        # Fish interaction
        for fish in self.fishes:
            for other_fish in self.fishes:
                if fish != other_fish:
                    fish.interact(other_fish)
    # Screen color
    def draw(self):
        pyxel.cls(L_BLUE)

        for fish in self.fishes:
            fish.draw()

App()
