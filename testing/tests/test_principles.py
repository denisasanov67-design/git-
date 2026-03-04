import sys
# TODO make with "pip install -e"
sys.path.append("../src")

from math import (
    add,
    add_with_bug
)

def test_add():
    assert add(2,2) == 4

def test_bug_addtion_basic():
    assert add_with_bug(2,2) == 4
    print("Test BUG ADDTION PASSED")

if __name__ == "__main__":
    test_add()