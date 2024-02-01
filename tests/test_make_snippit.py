from lib.make_snippit import *

def test_make_snippet():
    words1 = "This is a test"
    assert make_snippet(words1) == "This is a test"

def test_make_snippet_two():
    words2 = "This is a longer sentence to demonstrate the function."
    assert make_snippet(words2) == "This is a longer sentence ..." 

def test_make_snippet_three():
    words3 = "This is a longer sentance."  
    assert make_snippet(words3) == "This is a longer sentance."

def test_make_snippet_four(): 
    words4 = "" 
    assert make_snippet(words4)  == ""
   

                    