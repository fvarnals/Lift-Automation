import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from building import Building

def test_initialization():
    try:
        building = Building()
    except:
        pytest.fail("Failed to initialize Building object")
