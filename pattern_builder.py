class House:
    def __init__(self):
        self._walls = None
        self._roof = None
        self._windows = None

    def set_walls(self, walls):
        self._walls = walls

    def set_roof(self, roof):
        self._roof = roof

    def set_windows(self, windows):
        self._windows = windows

    def __str__(self):
        return f"House with {self._walls} walls, {self._roof} roof and {self._windows} windows"


class HouseBuilder:
    def __init__(self):
        self._house = House()

    def build_walls(self):
        pass

    def build_roof(self):
        pass

    def build_windows(self):
        pass

    def get_house(self):
        return self._house


class BrickHouseBuilder(HouseBuilder):
    def build_walls(self):
        self._house.set_walls("brick")

    def build_roof(self):
        self._house.set_roof("tile")

    def build_windows(self):
        self._house.set_windows("wooden")


class WoodenHouseBuilder(HouseBuilder):
    def build_walls(self):
        self._house.set_walls("wooden")

    def build_roof(self):
        self._house.set_roof("straw")

    def build_windows(self):
        self._house.set_windows("glass")


class HouseDirector:
    def __init__(self, builder):
        self._builder = builder

    def build(self):
        self._builder.build_walls()
        self._builder.build_roof()
        self._builder.build_windows()


builder = BrickHouseBuilder()
director = HouseDirector(builder)
director.build()
house = builder.get_house()
print(house)

builder = WoodenHouseBuilder()
director = HouseDirector(builder)
director.build()
house = builder.get_house()
print(house)