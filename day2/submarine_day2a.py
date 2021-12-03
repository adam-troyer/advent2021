from dataclasses import dataclass


@dataclass
class Coord3d:
    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class Submarine:
    position: Coord3d = Coord3d(0, 0, 0)

    def move(self, direction: str, distance: int) -> None:
        if direction == "forward":
            self.position.x += distance
        elif direction == "up":
            self.position.z -= distance
        elif direction == "down":
            self.position.z += distance
