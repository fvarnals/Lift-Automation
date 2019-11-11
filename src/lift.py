class Lift(object):

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.floors = list(range(0,len(queues)))
        self.occupants = []
        self.current_floor = 0
        self.queues = {}
        self.direction_of_travel = 'up'
        self.destination_floor = None
        self.empty = 'true'
        self.journey_history = []

        # initialize list of people queuing on each floor
        floor_number = 0
        for queue in queues:
            self.queues[floor_number] = queue
            floor_number += 1

    def number_of_passengers_queueing(self):
        passengers_queueing = 0
        queues = self.queues
        for queue in queues:
            for passenger in queues[queue]:
                passengers_queueing += 1
        return passengers_queueing

    def number_of_occupants(self):
        return len(self.occupants)

    def destination(self):
        return self.destination_floor

    def load_passenger(self, passenger):
        # passenger enters lift
        self.occupants.append(passenger)


    def unload(self):
        # all occupants destined for given floor, exit lift
        for passenger in reversed(self.occupants):
            if passenger == self.current_floor:
                self.occupants.remove(passenger)

    def go_up(self):
        next_floor = min(floor for floor in self.occupants if floor > self.current_floor)
        self.current_floor = next_floor

    def go_down(self):
        next_floor = max(floor for floor in self.occupants if floor < self.current_floor)
        self.current_floor = next_floor

    def passengers_pickup(self):
        temp_list = ()
        floor_queue = self.queues[self.current_floor]
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
        capacity = self.capacity
        asdf = self.number_of_occupants()
        return (asdf < capacity)


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
            if queue == ():
                pass
            else:
                self.current_floor = floor

    def smart_travel(self):
        if self.direction_of_travel == 'up':
            self.travel_to_highest_called_floor()
        else:
            self.travel_to_lowest_called_floor()
        if self.direction_of_travel == 'up':
            self.direction_of_travel = 'down'
        else:
            self.direction_of_travel = 'up'

    def set_direction_of_travel(self):
        if self.current_floor < self.destination_floor:
            self.direction_of_travel = 'up'
        elif self.current_floor > self.destination_floor:
            self.direction_of_travel = 'down'
        else:
            pass

    def record_stop(self):
        self.journey_history.append(self.current_floor)

    def return_to_ground_floor(self):
        self.current_floor = 0
