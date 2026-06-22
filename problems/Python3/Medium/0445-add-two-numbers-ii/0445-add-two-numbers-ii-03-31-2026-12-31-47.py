# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=None
        cur=None
        carry=0
        num1=self.reverse(l1)
        num2=self.reverse(l2)
        while (num1 or num2 or carry):
            sumval=carry
            if num1:
                sumval+=num1.val
                num1=num1.next
            if num2:
                sumval+=num2.val
                num2=num2.next
            newnode = ListNode(sumval%10)
            carry=sumval//10
            if res is None:
                res=newnode
                cur=newnode
            else:
                cur.next=newnode
                cur=cur.next
        return self.reverse(res)