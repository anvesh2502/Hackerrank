/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
  // Complete this method
  Node *prev=NULL,*next=head->next;
  Node *curr=head;
  while(curr!=NULL)
  {
  next=curr->next;
  curr->next=prev;
  prev=curr;
  curr=next;
  }
  return prev;

}
