from pysistence import Plist


def test_iteration():
    plist = Plist([1, 2, 3])
    assert [1, 2, 3] == [i for i in plist]

def test_tail():
    plist = Plist([1, 2, 3])
    assert 3 == plist.tail.value

def test_length():
    plist = Plist([1, 2, 3])
    assert 3 == len(plist)