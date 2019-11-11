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
    assert lift.occupants == []

def test_queues():
    assert lift.queues == {0:(), 1:(), 2: (5,5,5), 3:(), 4:(3,), 5:(), 6:()}

def test_number_of_passengers_queueing():
    assert lift.number_of_passengers_queueing() == 4

def test_load_passenger():
    lift.load_passenger(5)
    assert lift.occupants == [5]

def test_go_up():
    lift.occupants = [5,6,4]
    lift.go_up()
    assert lift.current_floor == 4

def test_go_down():
    lift.occupants = [1,3,2,1]
    lift.current_floor = 6
    lift.go_down()
    assert lift.current_floor == 3

def test_unload():
    lift.occupants = [2,1,2,5,2,5,4]
    lift.current_floor = 2
    lift.unload()
    assert lift.occupants == [1,5,5,4]

def test_empty_unload():
    lift.occupants = []
    lift.current_floor = 2
    lift.unload()

def test_passengers_pickup_going_up():
    lift = Lift(queues, 2)
    lift.current_floor = 2
    lift.passengers_pickup()
    assert lift.number_of_occupants() == 2
    assert lift.occupants == [5,5]
    assert lift.queues == {0:(), 1:(), 2: (5,), 3:(), 4:(3,), 5:(), 6:()}

def test_passengers_pickup_going_down():
    lift = Lift(queues, 2)
    lift.direction_of_travel = 'down'
    lift.current_floor = 4
    floor_queue = lift.queues[4]
    lift.passengers_pickup()
    assert lift.occupants == [3]
    assert lift.queues == {0:(), 1:(), 2: (5,5,5), 3:(), 4:(), 5:(), 6:()}

def test_passengers_pickup_no_queue():
    lift = Lift(queues, 2)
    lift.direction_of_travel = 'down'
    lift.current_floor = 1
    floor_queue = lift.queues[1]
    lift.passengers_pickup()
    assert lift.occupants == []

def test_set_destination():
    lift.set_destination(3)
    assert lift.destination_floor == 3

def test_travel_to_lowest_called_floor():
    lift.travel_to_lowest_called_floor()
    assert lift.current_floor == 2

def test_travel_to_highest_called_floor():
    lift.travel_to_highest_called_floor()
    assert lift.current_floor == 4

def test_smart_travel():
    lift = Lift(queues, capacity)
    lift.direction_of_travel = 'up'
    lift.smart_travel()
    assert lift.current_floor == 4

    lift.direction_of_travel = 'down'
    lift.smart_travel()
    assert lift.current_floor == 2

def test_set_direction_of_travel():
    lift.destination_floor = 3
    lift.current_floor = 0
    lift.set_direction_of_travel()
    assert lift.direction_of_travel == 'up'

    lift.destination_floor = 2
    lift.current_floor = 3
    lift.set_direction_of_travel()
    assert lift.direction_of_travel == 'down'

def test_journey_history():
    lift = Lift(queues, capacity)
    lift.current_floor = 0
    lift.record_stop()
    lift.current_floor = 6
    lift.record_stop()
    lift.current_floor = 3
    lift.record_stop()
    assert lift.journey_history == [0,6,3]

def test_unload_and_pickup():
    lift.occupants = [3]
    lift.current_floor = 3
    lift.direction_of_travel = 'down'
    lift.queues[3] = (5,5,5)
    lift.unload()
    lift.passengers_pickup()
    assert lift.occupants == [5,5,5]
