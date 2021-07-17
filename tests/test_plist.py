from pysistence import Plist

def test_iteration():
    plist = Plist([1,2,3])
    assert [1,2,3] == [i for i in plist]

