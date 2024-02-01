from lib.improve_grammar import *

def test_improve_grammar_one():
    assert improve_grammar ("my first test") == "no capital"

def test_improve_grammar_two():
    assert improve_grammar ("My first test") == "no punctuation" 

def test_improve_grammar_three():
    assert improve_grammar ("My first test.") == "sentance is fine"   
        
def test_improve_grammar_four():
    assert improve_grammar ("My first test*") == "no punctuation"       




    