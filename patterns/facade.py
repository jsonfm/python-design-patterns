"""
Type: Structural Pattern
Description: It provides a simplified (but limited) interface to a complex system of classes, library or framework
"""


class Cutter(object):
    def cut(self):
        print("cutting vegetables!")


class Boiler(object):
    def boil(self):
        print("boiling vegetables!")


class Frier(object):
    def fry(self):
        print("frying vegetables!")


class Cook(object):
    "Facade"

    def prepare_dish(self):
        self.cutter = Cutter()
        self.boiler = Boiler()
        self.frier = Frier()

        self.cutter.cut()
        self.boiler.boil()
        self.frier.fry()
