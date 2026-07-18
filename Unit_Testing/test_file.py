from calculate_grade import grade
def test_checking():
    assert grade(1000) == "Out of range"
    assert grade(100) == "A"
    assert grade(84) == "B"
    assert grade(70) == "C"
    assert grade(56) == "D"
    assert grade(30) == "F"

from dividing import divide
def test_positive():
   assert divide(5,5) == 1
   assert divide(10,2) == 5
def test_negative():
   assert divide(-5,-5) == 1.0
   assert divide(-10,-2) == 5.0
def ZeroDiv():
   assert divide(5,0) == ZeroDivisionError


from is_even import is_even
def test_is_positive():
  assert is_even(2) == True
  assert is_even(1) == False
def test_is_negative():
   assert is_even(-91) == False
   assert is_even(-6) == True

from greeting import greet
def test_default():
    assert greet() == "Hello, world" 
def test_argument():
    assert greet("Sugaina") == "Hello, Sugaina" 

from largest import maximum
def test_positive():
   assert maximum(3,5) == 5
   assert maximum(5,2) == 5
   assert maximum(5,5) == "equal"
   assert maximum(-5,-3) == -3
