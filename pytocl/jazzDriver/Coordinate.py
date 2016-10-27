class Coordinate:
    def __init__(self, distance, angle):
        self._distance = distance
        self._angle = angle

    @property
    def distance(self):
        return self._distance

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value

    @distance.setter
    def distance(self, value):
        self._distance = value