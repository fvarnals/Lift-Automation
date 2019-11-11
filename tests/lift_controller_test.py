import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from lift_controller import LiftController
from lift import Lift

queues = ( (),   (),    (), (),   (3,),    (),    () )
capacity = 5
lift = Lift(queues,capacity)
lift_controller = LiftController(lift)

def test_people_queueing():
    assert lift_controller.people_queueing == True

def test_people_in_lift():
    assert lift_controller.people_in_lift == False

def test_empty_travel():
    lift_controller.empty_travel(lift)
    assert lift.journey_history == [4]
    assert lift.occupants == [3]
    assert lift.destination_floor == 3

def test_travel_to_destination_floor():
    lift.occupants = [1,2,3]
    lift.direction_of_travel = 'down'
    lift.current_floor = 4
    lift.destination_floor = 1
    lift_controller.travel_to_destination_floor(lift)
    assert lift.journey_history == [4,3,2,1]

def test_return_to_ground_floor():
    lift.return_to_ground_floor()
    assert lift.current_floor == 0
