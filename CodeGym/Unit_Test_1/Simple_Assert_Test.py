import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5
    
def test_sqrt_faied():
    num = 25
    assert math.sqrt(num) == 6
	
def test_square():
    num = 7
    assert 7*7 == 50
	
def test_equality():
    assert 10==10