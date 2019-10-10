import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../lift')

from lift import Lift

queues = ( (),   (),    (5,5,5), (),   (),    (),    () )
capacity = 5

def test_initialization():
    try:
        lift = Lift(queues,capacity)
    except:
        pytest.fail("Failed to initialize Lift object")

lift = Lift(queues,capacity)

def test_capacity():
    assert lift.capacity == 5

def test_floors():
    assert lift.floors == [0,1,2,3,4,5,6]

def test_occupants():
    assert lift.occupants == {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

def test_load():
    lift.load(5)
    assert lift.occupants[5] == 1

def test_update_number_of_occupants():
    lift.update_number_of_occupants()
    assert lift.number_of_occupants == 1
