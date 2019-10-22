import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from lift import Lift

queues = ( (),   (),    (5,5,5), (),   (3),    (),    () )
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

def test_queues():
    assert lift.queues[2] == (5,5,5)

def test_load_passenger():
    lift.load_passenger(5)
    assert lift.occupants[5] == 1

def test_update_number_of_occupants():
    lift.update_number_of_occupants()
    assert lift.number_of_occupants == 1

def test_go_up():
    lift.go_up()
    assert lift.current_floor == 1

def test_go_down():
    lift.go_down()
    assert lift.current_floor == 0

def test_passengers_pickup():
    lift = Lift(queues, 2)
    lift.passengers_pickup((5,5,5))
    assert lift.number_of_occupants == 2
    assert lift.occupants[5] == 2

def test_set_destination():
    lift.set_destination(3)
    assert lift.destination_floor == 3

def test_travel_to_lowest_called_floor():
    lift.travel_to_lowest_called_floor()
    assert lift.current_floor == 2

def test_travel_to_highest_called_floor():
    lift.travel_to_highest_called_floor()
    assert lift.current_floor == 4

def test_set_direction_of_travel():
    lift.destination_floor = 3
    lift.current_floor = 0
    lift.set_direction_of_travel()
    assert lift.direction_of_travel == 'up'

    lift.destination_floor = 2
    lift.current_floor = 3
    lift.set_direction_of_travel()
    assert lift.direction_of_travel == 'down'

def test_travel():
    lift.current_floor = 2
    lift.destination_floor = 5
    lift.travel()
    assert lift.current_floor == 5
