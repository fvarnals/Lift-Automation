class Lift(object):

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.floors = list(range(0,len(queues)))
        self.occupants = {}
        self.number_of_occupants = 0
        self.current_floor = 0
        self.queues = {}
        self.direction_of_travel = 'up'
        self.destination_floor = None
        self.empty = 'true'

        # initialize list of occupants by desired destination floor
        for floor in self.floors:
            self.occupants[floor] = 0

        # initialize list of people queuing on each floor
        floor_number = 0
        for queue in queues:
            self.queues[floor_number] = queue
            floor_number += 1

    def load_passenger(self, destination_floor):
        # passenger enters lift
        self.occupants[destination_floor] += 1
        self.queues[self.current_floor]
        self.update_number_of_occupants()

    def unload(self, floor):
        # all occupants destined for given floor, exit lift
        self.occupants[floor] = 0

    def update_number_of_occupants(self):
        # update the number of people currently in the lift
        self.number_of_occupants = sum(self.occupants.values())

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        self.current_floor -= 1

    def passengers_pickup(self, floor_queue):
        temp_list = ()
        for passenger in floor_queue:
            if (self.has_spaces_available()) and (self.direction_suitable_for(passenger)):
                self.load_passenger(passenger)
            else:
                temp_list += (passenger,)
        self.queues[self.current_floor] = temp_list

    def direction_suitable_for(self, passenger):
        if self.direction_of_travel == 'up':
            return passenger > self.current_floor
        else:
            return passenger < self.current_floor

    def has_spaces_available(self):
        return self.number_of_occupants < self.capacity

    def set_destination(self, floor):
        self.destination_floor = floor

    def travel_to_lowest_called_floor(self):
        for floor in self.queues:
            queue = self.queues[floor]
            if queue == ():
                pass
            else:
                self.current_floor = floor
                break

    def travel_to_highest_called_floor(self):
        for floor in self.queues:
            queue = self.queues[floor]
            print(queue)
            if queue == ():
                pass
            else:
                self.current_floor = floor

    def set_direction_of_travel(self):
        if self.current_floor < self.destination_floor:
            self.direction_of_travel = 'up'
        elif self.current_floor > self.destination_floor:
            self.direction_of_travel = 'down'
        else:
            pass
