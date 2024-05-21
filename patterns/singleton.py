"""
Type: Creational Pattern
Description: It ensures that a class has only one instance
"""


class Singleton(object):
    """Singleton design pattern."""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
