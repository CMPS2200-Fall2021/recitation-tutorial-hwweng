def sum_of_squares(a):
        sum = 0
        for i in a:
                sum = sum + i*i
        return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
    assert sum_of_squares([4,5,6]) == 77

test_one()
test_two()
