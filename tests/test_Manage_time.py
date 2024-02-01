from lib.manage_time import *

def test_reading_time ():
    assert reading_time (300, 200) == "1mins 30seconds"

def test_reading_time_two ():
    assert reading_time (450, 200) == "2mins 15seconds"    

def test_reading_time_three ():
    assert reading_time (5000, 200) == "25mins 0seconds"     

def test_reading_time_four ():
    assert reading_time ("300", 200) == "1mins 30seconds" 

def test_reading_time_five ():
    assert reading_time ("hundred", 200) == "cannot work this out" 

def test_reading_time_six ():
    assert reading_time (500, "hundred") == "cannot work this out"  

def test_reading_time_seven():
    assert reading_time (-50, 200) == "cannot work this out"         
             




