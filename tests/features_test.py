import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from lift_controller import LiftController
from lift import Lift

queues = ( (),   (),    (5,5,5), (),   (3,),    (),    () )
capacity = 5
lift = Lift(queues,capacity)
lift_controller = LiftController(lift)

def test_empty_travel():
    lift_controller.empty_travel(lift)
    assert lift.journey_history == [4]
    assert lift.occupants == [3]
    assert lift.direction_of_travel == 'down'
    assert lift.destination_floor == 3

def test_run():
    lift = Lift(queues,capacity)
    lift_controller = LiftController(lift)
    lift_controller.run(lift)
    assert lift.journey_history == [0,4,3,2,5,0]

queues2 = ( (),   (0,),  (),      (),   (2,),  (3,),  () )
lift2 = Lift(queues2,capacity)
lift_controller2 = LiftController(lift2)

def test_run_2():
    lift_controller2.run(lift2)
    assert lift2.journey_history == [0, 5, 4, 3, 2, 1, 0]
