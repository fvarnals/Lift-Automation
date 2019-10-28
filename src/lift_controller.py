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
