import pytest
from working_lab.Lab10_ndecker5_1 import degree_rotation

def test_positive_degree_rotation_input():
    assert degree_rotation(100)
    assert degree_rotation(460)
    assert degree_rotation(820)

def test_negative_degree_rotation_negative_input():
    assert degree_rotation(-100)
    assert degree_rotation(-460)
    assert degree_rotation(-820)

def test_negative_degree_rotation_empty_input():
    with pytest.raises(TypeError) as i:
        degree_rotation()
    assert str(i.value) == "degree_rotation() missing 1 required positional argument: 'number'"

def test_negative_degree_rotation_string_input():
    with pytest.raises(TypeError) as i:
        degree_rotation("Lab 10")
    assert str(i.value) == "Number must be an int or float"

def test_negative_degree_rotation_boolean_input():
    with pytest.raises(TypeError) as i:
        degree_rotation(True)
    assert str(i.value) == "Number must be an int or float"

