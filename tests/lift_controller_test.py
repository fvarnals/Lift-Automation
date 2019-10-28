import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from lift_controller import LiftController
from lift import Lift

queues = ( (),   (),    (), (),   (3,),    (),    () )
capacity = 5


def test_lift_active():
        lift = Lift(queues,capacity)
        lift_controller = LiftController(lift)
        assert lift_controller.people_queueing == True
