import pytest
from src.prj1.main import add

def test_add_positive():
    assert add(5,3) == 8 