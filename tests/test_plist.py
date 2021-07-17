from pysistence import Plist


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
    assert len(concatenated_list) > len(plist)
    assert concatenated_list.head == plist.head
    assert concatenated_list.tail != plist.tail


def test_representation():
    plist = Plist([1, 2, 3])
    assert plist.__repr__() == "Plist[1, 2, 3]"


def test_length():
    plist = Plist([1, 2, 3])
    assert len(plist) == 3
