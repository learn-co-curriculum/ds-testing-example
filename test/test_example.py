import pytest
import os
os.path.join(os.path.dirname(__file__), '..')
# import xgboost
import keras
# Modify system path so test can find the notebook




from ipynb.fs.full.index import two_plus_two

def test_two_plus_two():
    assert two_plus_two == 4
