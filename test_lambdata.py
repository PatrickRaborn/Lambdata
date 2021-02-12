"""Basic unit test for lambdata package"""

from random import randint
import pytest
import lambdata as ld


def test_increment_int():
    '''Making sure increment works'''
    x0 = 0
    y0 = ld.increment(x0) # 1
    assert y0 == 1


def test_increment_float():
    '''Making sure increment works for float'''
    x0 = 10.5
    y0 = ld.increment(x0) # 11.5
    assert y0 == 11.5

def test_increment_neg():
    '''Making sure increment works for neg floats'''
    x0 = -1.5
    y0 = ld.increment(x0) # -1.5
    assert y0 == -1.5


def test_colors():
    '''Testing COLORS contains correct items'''
    assert 'Cyan' in ld.COLORS
    assert 'Muave' in ld.COLORS
    assert 'Brown' not in ld.COLORS

def test_number_colors():
    assert len(ld.COLORS) == 4 
