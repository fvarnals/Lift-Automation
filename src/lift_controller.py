from lift import Lift

class LiftController(object):

    def __init__(self, lift):
        lift = lift

    def people_in_lift(self,lift):
        n_occupants = lift.number_of_occupants()
        if n_occupants > 0:
            return True
        else:
            return False

    def people_queueing(self,lift):
        n_queueing = lift.number_of_passengers_queueing()
        if n_queueing > 0:
            return True
        else:
            return False

    def start(self,lift):
        lift.record_stop()
        lift.unload()
        lift.passengers_pickup()
        if lift.number_of_occupants() > 0:
            lift.set_destination(lift.occupants[0])

    def empty_travel(self,lift):
        lift.smart_travel()
        lift.record_stop()
        lift.passengers_pickup()
        lift.set_destination(lift.occupants[0])
        lift.set_direction_of_travel()

    def run(self,lift):
        self.start(lift)
        while (self.people_in_lift(lift)) or (self.people_queueing(lift)):
            if lift.number_of_occupants() == 0:
                self.empty_travel(lift)
            self.travel_to_destination_floor(lift)
        lift.return_to_ground_floor()
        lift.record_stop()

    def travel_to_destination_floor(self, lift):
        while lift.current_floor != lift.destination_floor:
            if lift.direction_of_travel == 'up':
                lift.go_up()
            else:
                lift.go_down()

            lift.record_stop()
            lift.unload()
            lift.passengers_pickup()
        if len(lift.occupants) > 0:
            lift.set_destination(lift.occupants[0])
        lift.set_direction_of_travel()
