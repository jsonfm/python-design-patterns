from patterns.singleton import Singleton


def test_singleton():
    object1 = Singleton()
    object2 = Singleton()
    assert object1 is object2, "Objects are different!"