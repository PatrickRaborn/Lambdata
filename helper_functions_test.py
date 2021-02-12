"""Basic unit test for helper_functions package"""

import pandas as pd 
import numpy as np
import pytest
from lambdata.helper_functions import LambdaClass as LC
from pydataset import data

df = data('titanic') # Dataset example from which to run test


def test_null():
    '''Test that output is dataframe dtype and integer'''
    df_null = LC.null_count(df)
    assert isinstance(df_null, np.int64)

def test_split():
    '''Test split function output as dataframe dtype'''
    train, test = LC.train_test_split(df, .8)
    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)

