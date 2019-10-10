class Lift(object):

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.floors = list(range(0,len(queues)))
        self.occupants = {}

        # initialize list of occupants by desired destination floor
        for floor in self.floors:
            self.occupants[floor] = 0

    def load(self, passenger):
        self.occupants[passenger] += 1

    def unload(self, level):
        self.occupants[level] = 0
