import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from lift import Lift

queues = ( (),   (),    (5,5,5), (),   (3,),    (),    () )
capacity = 5
