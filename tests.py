""" Tests for maths.py """
import pytest

from maths import sumar

def test_sumar_numeros():
    """ Test sumando 2 numeros """
    assert 8 == sumar(3,5)

def sumar(x,y):
    return x + y


