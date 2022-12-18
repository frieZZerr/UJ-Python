from singlelist import Node, SingleList

def range_char(start, stop):
    return ( chr(n) for n in range( ord(start), ord(stop) + 1) )

def test_insert_head():
    list = SingleList()
    list.insert_head( Node("A") )
    list.insert_head( Node("B") )
    list.insert_head( Node("C") )

    assert list.head.data == "C"
    assert list.head.next.data == "B"
    assert list.tail.data == "A"
    assert list.tail.next == None
    assert list.length == 3

def test_insert_tail():
    list = SingleList()
    list.insert_tail( Node("A") )
    list.insert_tail( Node("B") )
    list.insert_tail( Node("C") )

    assert list.head.data == "A"
    assert list.head.next.data == "B"
    assert list.tail.data == "C"
    assert list.tail.next == None
    assert list.length == 3

def test_remove_head():
    list = SingleList()
    list.insert_head( Node("A") )
    list.insert_head( Node("B") )
    list.insert_head( Node("C") )

    assert list.remove_head().data == "C"
    assert list.length == 2
    assert list.remove_head().data == "B"
    assert list.length == 1
    assert list.remove_head().data == "A"
    assert list.length == 0

def test_remove_tail():
    list = SingleList()
    list.insert_tail( Node("A") )
    list.insert_tail( Node("B") )
    list.insert_tail( Node("C") )
   
    assert list.remove_tail().data == "C"
    assert list.length == 2
    assert list.remove_tail().data == "B"
    assert list.length == 1
    assert list.remove_tail().data == "A"
    assert list.length == 0

def test_join():
    list1 = SingleList()
    list1.insert_tail( Node("A") )
    list1.insert_tail( Node("B") )
    list1.insert_tail( Node("C") )

    list2 = SingleList()
    list2.insert_tail( Node("D") )
    list2.insert_tail( Node("E") )
    list2.insert_tail( Node("F") )
    list1.join(list2)

    assert list2.count() == 0

    for i in range_char("A", "F"):
        assert list1.remove_head().data == i

def test_clear():
    list = SingleList()
    list.insert_tail( Node("A") )
    list.insert_tail( Node("B") )
    list.insert_tail( Node("C") )
    list.clear()
    
    assert list.head is None
    assert list.tail is None
    assert list.count() == 0

test_insert_head()
test_insert_tail()
test_remove_head()
test_remove_tail()
test_join()
test_clear()