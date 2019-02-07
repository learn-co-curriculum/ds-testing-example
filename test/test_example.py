# # Modify system path so test can find the notebook
# import os
# path = os.path.split(os.getcwd())
#
# os.chdir(path[0])
# print(os.getcwd())

from ipynb.fs.full.index import q1, q2, q3, q4

def test_q1():
    assert q1 == 4

def test_q2():
    assert q2 == 10

def test_q3():
    assert q3 <= 16

def test_q4():
    assert q4 == True
