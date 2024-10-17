import ci_course
import pytest

def test_greet():
    """
    Test the function `greet` in functionality.py
    """
    assert ci_course.greet() == "Hello "
    assert ci_course.greet("Fergus") == "Hello Fergus"


def test_minimum():
    """
    Test the function `minimum` in functionality.py
    """
    assert ci_course.minimum(1, 2, 3) == 1
    assert ci_course.minimum(1.2, 2.3) == 1.2
    assert ci_course.minimum(-1.2, -3) == -3
    assert ci_course.minimum(1, "Hello", [1,2,3]) == 1

    with pytest.raises(TypeError):
        ci_course.minimum("Hello", "Oh no", [1,3,4]) 

    
