import pytest
from myproj import predictor


@pytest.mark.parametrize("a_var", [
        (1),
        (2),
        (3)
    ])
def test_myclass(a_var):
    my_obj = predictor.MyClass(a_var)
    assert my_obj.get_my_var() == a_var
    assert my_obj.myvar == a_var
