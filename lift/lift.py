class Lift(object):

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.floors = list(range(0,len(queues)))
        self.occupants = {}
        self.number_of_occupants = 0

        # initialize list of occupants by desired destination floor
        for floor in self.floors:
            self.occupants[floor] = 0

    def load(self, passenger):
        # passenger enters lift
        self.occupants[passenger] += 1

    def unload(self, level):
        # all occupants destined for given floor, exit lift
        self.occupants[level] = 0

    def update_number_of_occupants(self):
        # update the number of people currently in the lift
        self.number_of_occupants = sum(self.occupants.values())
