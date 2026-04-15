# The Pragmatic Programmer — DRY leniency: caching for performance.
# Translated from the book's Java `Line` example.
#
# DRY isn't about code. It's about truth — one fact, one place, one owner.
# Caching duplicates the "length" fact, but the violation is contained:
# only methods inside the class touch the cache, so callers can't see the lie.

import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return math.hypot(other.x - self.x, other.y - self.y)


# Version 1: length computed on every call. Always truthful.
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def length(self) -> float:
        return self.start.distance_to(self.end)


# Version 2: length cached. DRY violation sealed inside the class —
# every mutator refreshes the cache, so outside code can't observe a stale value.
class LineCached:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self._calculate_length()

    # public
    def set_start(self, p: Point) -> None:
        self.start = p
        self._calculate_length()

    def set_end(self, p: Point) -> None:
        self.end = p
        self._calculate_length()

    def get_start(self) -> Point:
        return self.start

    def get_end(self) -> Point:
        return self.end

    def get_length(self) -> float:
        return self.length

    # private
    def _calculate_length(self) -> None:
        self.length = self.start.distance_to(self.end)


def main() -> None:
    a = Point(0, 0)
    b = Point(3, 4)

    line = Line(a, b)
    print(f"Line.length()         = {line.length()}")

    cached = LineCached(a, b)
    print(f"LineCached.get_length() = {cached.get_length()}")

    cached.set_end(Point(6, 8))
    print(f"after set_end           = {cached.get_length()}")


if __name__ == "__main__":
    main()
