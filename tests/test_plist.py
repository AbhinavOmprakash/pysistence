from pysistent import Plist
from pysistent.plist import ListNode

def test_list_node():
    n1 = ListNode(1)
    n2 = ListNode(2)
    assert n1 != n2
    assert n1 < n2
    assert n2 > n1

    assert str(n1) == "1"
    
    n1.next = n2
    assert str(n1.next) == "2"




def test_iteration():
    plist = Plist([1, 2, 3]) 
    assert [i for i in plist] == [1, 2, 3]


def test_tail():
    plist = Plist([1, 2, 3])
    assert plist.tail.value == 3


def test_cons():
    plist = Plist([1, 2, 3])
    cons_plist = plist.cons(0)
    assert cons_plist.head.value == 0
    assert cons_plist.head != plist.head
    assert cons_plist.head.next == plist.head
    assert cons_plist.tail == plist.tail
    assert len(cons_plist) > len(plist)


def test_conj():
    plist = Plist([1, 2, 3])
    cons_plist = plist.conj(0)
    assert cons_plist.head.value == 0
    assert cons_plist.head != plist.head
    assert cons_plist.head.next == plist.head
    assert cons_plist.tail == plist.tail
    assert len(cons_plist) > len(plist)


def test_concat():
    plist = Plist([1, 2, 3])
    concatenated_list = plist.concat(4)
    assert concatenated_list.tail.value == 4
    assert concatenated_list.head == plist.head
    assert concatenated_list.tail != plist.tail
    assert len(concatenated_list) > len(plist)


def test_representation():
    plist = Plist([1, 2, 3])
    assert plist.__repr__() == "Plist[1, 2, 3]"


def test_length():
    plist = Plist([1, 2, 3])
    assert len(plist) == 3

def test_eq():
    pl1 = Plist([1, 2, 3,4])
    pl2 = Plist([1, 2, 3,4])
    assert pl1 == pl2

    pl1 = Plist([1, 2, 3])
    pl2 = Plist([1, 2, 3,4])
    assert not pl1 == pl2


def test_lt():
    pl1 = Plist([1, 2, 3])
    pl2 = Plist([1, 2, 3,4])
    assert pl1 < pl2

    pl1 = Plist([0,1, 2, 3])
    pl2 = Plist([1, 2, 3,4])
    assert pl1 < pl2

    pl1 = Plist([0,3, 2, 3])
    pl2 = Plist([1, 2, 3,4])
    assert pl1 < pl2

    pl1 = Plist([1, 2, 3,4])
    pl2 = Plist([1, 2, 3,4])
    assert not pl1 < pl2
    assert not pl1 > pl2