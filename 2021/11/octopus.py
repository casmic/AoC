class Octopus:

    def __init__(self, energy = 0, x = -1, y = -1) -> None:
        self._energy = energy
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"energy: {self._energy} - X: {self._x} - Y: {self._y}"

    def Step(self):
        self._energy += 1
        if(self._energy == 10):
            return True
        else:
            return False

    def Reset(self):
        if(self._energy > 9):
            self._energy = 0