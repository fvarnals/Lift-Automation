class Lift(object):

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.floors = list(range(0,len(queues)))
        pass
