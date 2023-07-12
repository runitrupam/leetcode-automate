class MyLinkedList {
public:
    /** Initialize your data structure here. */
     struct Node {
        int val;
        Node* next;
        Node(int value) {
            next = NULL;
            val = value;
        }
    };
    
    Node *head;
    MyLinkedList() {
        head=NULL;
        
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        
        
         Node *t = head;
        int c =0;
            while(t != NULL )
            {
                if(c==index)
                return t->val;
             c++;
                t=t->next;
            }
           return -1;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
       Node *temp = new Node(val);
        
        if(head == NULL)
        {
            temp->next = NULL;
            head = temp;
        }
        else
        {
            temp -> next = head;
            head = temp;
        }
        
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
         Node *temp = new Node(val);
        temp->next = NULL;
        if (head == NULL)
        {
            head=temp;
        }
        else
        {
            Node *t = head;
            while(t->next != NULL)
            {
                t=t->next;
            }
            t->next = temp;
        }
            
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        int size =0;
         Node *t = head;
            while(t != NULL )
            {
                size++;
                t=t->next;
            }
        
        
         if (index == size)
         {addAtTail(val);
          return;
         }
        if(index == 0)
        {  addAtHead(val);
        return;
        }
         if (index > size)
            return ;
        
        
        Node *temp = new Node(val);
           t = head;
        Node *t2;
        int c =0;
            while(t != NULL )
            {
                
                
                if(c == index)
                break;
                
                t2=t;
                t=t->next;
                c++;
            }   
             t2->next = temp;
        temp->next = t;
               
        
        
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
              Node *t = head;
        Node *t2=NULL;
        int c = 0 ;
        if (index==0)
        {
            head = head->next;
            return;
        }
    
            
            while(t != NULL )
            {
                
                
                if(c == index)
                break;
                
                t2=t;
                t=t->next;
                c++;
            }  
            if(t!=NULL)
             t2->next = t->next;
       else
           return;
        }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */