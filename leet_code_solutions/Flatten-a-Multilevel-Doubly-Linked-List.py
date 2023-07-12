/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        Node *temp = head;
        Node *H=NULL;
        Node *x;
        Node *y=NULL;
        while(temp != NULL)
        {
            if(temp->child == NULL)
            {
                if(H==NULL)
                {
                    H=temp;
                    x=H;
                    
                }
                else
                {
                    x->next=temp;
                    x=x->next;
                }
             
              temp=temp->next;  
            }
            
            else
            {
                if(H==NULL)
                {   
                    H=temp;
                    x=H;
                    
                }
                else
                {   
                    x->next=temp;
                    x=x->next;
                }
                y=temp;
                temp=temp->next;
                x->next = flatten(y->child);
                y->child = NULL;
                x=x->next;
                
                if(x!=NULL)
                x->prev = y;
                
                if(x!=NULL)
                while(x->next != NULL)
                {
                    x=x->next; 
                }
                if(temp != NULL)
                    temp->prev = x;
                if(x!=NULL)
                x->next = temp;
                    
                
            }
            
        }
        
        return H;
        
    }
};