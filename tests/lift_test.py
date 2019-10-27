import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from lift import Lift

queues = ( (),   (),    (5,5,5), (),   (3,),    (),    () )
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
    assert lift.queues == {0:(), 1:(), 2: (5,5,5), 3:(), 4:(3,), 5:(), 6:()}

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

def test_passengers_pickup_going_up():
    lift = Lift(queues, 2)
    lift.current_floor = 2
    lift.passengers_pickup((5,5,5))
    assert lift.number_of_occupants == 2
    assert lift.occupants[5] == 2
    assert lift.queues == {0:(), 1:(), 2: (5,), 3:(), 4:(3,), 5:(), 6:()}

def test_passengers_pickup_going_down():
    lift = Lift(queues, 2)
    lift.direction_of_travel = 'down'
    lift.current_floor = 4
    floor_queue = lift.queues[4]
    lift.passengers_pickup(floor_queue)
    assert lift.occupants[3] == 1
    assert lift.queues == {0:(), 1:(), 2: (5,5,5), 3:(), 4:(), 5:(), 6:()}

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


def test_destination_set_to_highest_called_floor_when_empty_and_going_up():
    lift.number_of_occupants = 0
    lift.current_floor = 1
    lift.direction_of_travel = 'up'
    lift.smart_travel()
    assert lift.current_floor == 4

def test_destination_set_to_lowest_called_floor_when_empty_and_going_up():
    lift.number_of_occupants = 0
    lift.current_floor = 1
    lift.direction_of_travel = 'up'
    lift.smart_travel()
    assert lift.current_floor == 4