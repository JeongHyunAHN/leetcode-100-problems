"""
    Pointers are often used about Python objects, 
    such as 

    when a function obtains a pointer 
    to an object from elsewhere or 

    when the values within Python objects 
    like lists and dictionaries are extracted.
"""

"""
    단순 연결 리스트 (Linked List)
    여기서 리스트의 가장 첫 번째에 위치한 노드를 Head, 끝에 위치한 노드를 Tail이라고 부른다.
    각 노드는 데이터(data)와 링크(link)라는 2가지 속성을 가진다.
    data: 노드에 저장된 데이터 값 (ex. 아래 그림에서 9, 17, 11)
    link: 연결된 다음 노드 주소 (ex. 아래 그림에서 화살표)
    여기서 Tail 노드의 다음 노드는 Nullptr을 가리키고 있다.
"""

################################################################################################

"""
    노드(node)는 "데이터(값) + 다음 노드의 주소(포인터)"를 담고 있는 형태로 이루어져 있는 녀석이다.

    # Node 생성 (data = 1)
    node1 = ListNode(1)

    # Node의 값과 포인터 출력
    print(node1.val)     # 1
    print(node1.next)    # None
"""

l1 = [2,4,3]
l2 = [5,6,4]

class ListNode:
    def __init__(self,data=0,next=None) -> ListNode:
        self.data = data
        self.next = next

class Solution:
    def addTwoNumbers(self,l1:Optional[ListNode],l2:Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry!=0:
            x = 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 값
        self.next = next    # 다음 노드의 주소

class LinkedList:
    def __init__(self, data):
        self.head = ListNode(data)
        
    # 새로운 노드 추가
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(data)
	
    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

"""
    여기서 보이는 헤드(head)는 연결 리스트 중에서도 가장 앞에 있는 노드를 의미한다.
    새로운 노드를 추가하는 append 메서드 같은 경우에는
    계속 노드를 헤드부터 반복/갱신하면서, 노드의 next값이 None이 나올 때 그 위치 노드의 next값에 새로운 데이터를 추가해주는 방식이다.
    마찬가지로 모든 노드 값을 추가하는 print_all 메서드도 계속 노드를 헤드부터 반복/갱신하면서, val값을 출력해주는 방식인 것을 확인할 수 있겠다.
"""
################################################################################################

"""
type hinting :
    The specification of data types in an otherwise untyped language, 
    to enforce variables having a particular type.

    Type hints in Python involve a colon and a type declaration 
    after the first invocation of a name in a namespace. 

    Here's an example: 

    name: str, age: int, name = input("Your name?"), age = int(input("Your age?")) 

    # alternatively, and more simply: 
    name: str = input("Your name?"), age: int = int(input("Your age?"))
"""

"""
    Optional[X] is equivalent to X | None (or Union[X, None]).
"""

"""
    A union type describes a value that can be one of several types. 
    We use the vertical bar ( | ) to separate each type, 
    so 
        number | string | boolean 
    is the type of a value that can be a number , a string , or a boolean .
"""

"""
    this is not the same concept as an optional argument, 
    which is one that has a default. 
    
    An optional argument with a default 
    does not require the Optional qualifier 
    on its type annotation just because it is optional. 
    
    On the other hand, if an explicit value of None is allowed, 
    the use of Optional is appropriate, 
    whether the argument is optional or not. 
"""