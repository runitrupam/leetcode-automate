/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    
    int count(ListNode *head)
    {
        
        
        ListNode* current = head; 
  
    
    int count = 0; 
  
    
    while (current != NULL) { 
  
       
        count++; 
  
      
        current = current->next; 
    } 
  
    return count; 
        
        
        
    }
        
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
     
        int c1,c2;
        int d;
        ListNode *current1;
        ListNode *current2;
        current1=headA;
        current2=headB;
        
        int i;
        
        c1=count(current1);
        c2=count(current2);
        
      
        
        if(c1>c2)
        {
            d=c1-c2;
         
        i=0;
        current1=headA;
        current2=headB;
        while(i < d)
        {
            if(current1 == NULL)
                return NULL;
            current1 = current1->next;
            i++;
        }
         
         while (current1 != NULL and current2 != NULL) { 
        if(current1 == current2) 
        { return current1; 
        }
        current1 = current1->next; 
        current2 = current2->next; 
    }    
         
         
         
        }
        else
           {
        d=c2-c1;
         
        i=0;
        current1=headA;
        current2=headB;
        while(i<d)
        {
            if (current2==NULL)
                return NULL;
            current2=current2->next;
            i++;
        }
         
         while (current1 != NULL && current2 != NULL)
         { 
             if (current1 == current2) 
             {return current2;} 
             
      
        current1 = current1->next; 
        current2 = current2->next; 
    }    
         
         
         
        }
        
       return NULL; 
    }
};