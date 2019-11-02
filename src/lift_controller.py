from lift import Lift

class LiftController(object):

    def __init__(self, lift):
        n_lift_occupants = lift.number_of_occupants
        n_people_queueing = lift.number_of_passengers_queueing()

        self.people_in_lift = (n_lift_occupants > 0)
        self.people_queueing = (n_people_queueing > 0)

    def start(self,lift):
        lift.record_stop()
        lift.unload()
        lift.passengers_pickup()

    def empty_travel(self,lift):
        lift.smart_travel()
        lift.record_stop()
        lift.passengers_pickup()
        lift.set_destination(lift.occupants[0])

    def run(self,lift):
        self.start(lift)
        while (self.people_in_lift) or (self.people_queueing):
            if lift.number_of_occupants == 0:
                self.empty_travel(lift)

    def travel_to_destination_floor(self, lift):
        while lift.current_floor != lift.destination_floor:
            if lift.direction_of_travel == 'up':
                lift.go_up()
                lift.record_stop()
                lift.unload()
                lift.passengers_pickup()
            else:
                lift.go_down()
                lift.record_stop()
                lift.unload()
                lift.passengers_pickup()
