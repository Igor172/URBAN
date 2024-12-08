from threading import Thread
import random
import time
from inspect import getmembers
import pprint


class Car(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.model = 'model'

    def run(self):
        time_to_wash = random.randint(5, 15)
        time.sleep(time_to_wash)


def introspection_info(obj):
    return {'type': type(obj), 'attributes and methods': dir(obj), 'module': getmembers(obj)}


if __name__ == '__main__':

    BMW = Car()
    pprint.pprint(introspection_info(BMW))