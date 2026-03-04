import sys
# TODO make with "pip install -e"
sys.path.append("../src")

from math_ad import (
    add,
    add_with_bug,
    add_something,
    calculation_tax
)

def test_add():
    assert add(2,2) == 4

def test_bug_addtion_basic():
    assert add_with_bug(2,2) == 4
    print("Test BUG ADDTION PASSED")

def dest_fest_addition_over():
    for i in range(0,2*32):
        for j in range(0,2*32):
            assert add (i,j) == i+j
            assert add(-i,j) == -i+j
            assert add(i,-j) == i-j
            assert add(-i,-j) == -i-j

def dest_fest_addition_resonable():
        assert add (6,3) == 9
        assert add (0,3) == 3
        assert add (0,-3) == -3
        assert add (-7,-83) == -90
        print("Test ADDITION with   REASON")

def test_add_sometising_reas():
     add_something(None,None) == 0
     add_something(None, 'abs') == 0  
     add_something(None, 10) == 0
     add_something(None, abs) == 0
     add_something("abs", 10) == "abs10"
     add_something(10, "abs") == "10abs"
     add_something("xyz", "abs") == "xyzabs"

def test_tax_calculation():
     assert calculation_tax(1000) == 150
     assert calculation_tax(2000) == 300
     assert calculation_tax(30) == 4.5
     print("Test TAX CALCUL")

def test_tax_calc_fight_():
     assert calculation_tax()
if __name__ == "__main__":
    test_add()
    test_bug_addtion_basic()
    dest_fest_addition_over()
    dest_fest_addition_resonable()
    test_add_sometising_reas()
    test_tax_calculation()