from lib.Make_snippit import *

def test_make_snippet():
    words1 = "This is a test"
    assert make_snippet(words1) == "This is a test"
                    