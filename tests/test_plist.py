from pysistence import Plist


def test_iteration():
    plist = Plist([1, 2, 3])
    assert [i for i in plist]==[1, 2, 3] 

def test_tail():
    plist = Plist([1, 2, 3])
    assert plist.tail.value==3

def test_cons():
    plist = Plist([1, 2, 3])
    cons_plist = plist.cons(0)
    assert len(cons_plist) > len(plist)
    assert cons_plist.head != plist.head
    assert cons_plist.head.next == plist.head
    assert cons_plist.tail == plist.tail
        
    
def test_representation():    
    plist = Plist([1, 2, 3])
    assert plist.__repr__()=="Plist[1, 2, 3]"

def test_length():
    plist = Plist([1, 2, 3])
    assert len(plist)==3

