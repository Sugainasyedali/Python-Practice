import pytest
def divide(a,b):
    if b==0 :
       pytest.raises(ZeroDivisionError)
    else:
        return a/b