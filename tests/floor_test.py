import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from floor import Floor

def test_initialization():
    try:
        floor = Floor()
    except:
        pytest.fail("Failed to initialize Lift object")

floor = Floor(4, (5,5,5))

def test_floor_queue():
    assert floor.queue == (5,5,5)
