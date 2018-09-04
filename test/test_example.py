# # Modify system path so test can find the notebook
# import os
# path = os.path.split(os.getcwd())
#
# os.chdir(path[0])
# print(os.getcwd())

from ipynb.fs.full.index import two_plus_two

def test_two_plus_two():
    assert two_plus_two == 4
