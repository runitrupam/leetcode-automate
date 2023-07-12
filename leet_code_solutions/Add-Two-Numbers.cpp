/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include<bits/stdc++.h>
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode *t1=l1;
        ListNode *t2=l2;
        ListNode *temp;
        ListNode *x;
        
        ListNode *head=NULL;
        int carry=0;int s;
        while(t1!=NULL and t2!=NULL)
        {
            s = t1->val + t2->val + carry; 
            
            if(s>9)
            {temp = new ListNode(s%10); 
                carry=s/10;
            }
            else{
                if((s )> 9)
                {   
                    temp = new ListNode((s )%10);
                    carry=1;
                }
                else
                {
                   
                    temp = new ListNode(s);
                    carry=0;
                }
                
            }
            if(head==NULL)
            {  head=temp;
                x=head;
            }
            else
            { x->next=temp;
            x=x->next;
            }
            t1=t1->next;
            t2=t2->next;
            
        }
        
        while(t1!=NULL)
        {
            s = t1->val  + carry; 
            
            if(s>9)
            {temp = new ListNode(s%10); 
                carry=s/10;
            }
            else{
                if((s )> 9)
                {   
                    temp = new ListNode((s )%10);
                    carry=1;
                }
                else
                {
                   
                    temp = new ListNode(s);
                    carry=0;
                }
                
            }
            if(head==NULL)
            {  head=temp;
                x=head;
            }
            else
            { x->next=temp;
            x=x->next;
            }
            t1=t1->next;
        }
        while(t2!=NULL)
        {
           s = t2->val + carry; 
            
            if(s>9)
            {temp = new ListNode(s%10); 
                carry=s/10;
            }
            else{
                if((s )> 9)
                {   
                    temp = new ListNode((s )%10);
                    carry=1;
                }
                else
                {
                   
                    temp = new ListNode(s);
                    carry=0;
                }
                
            }
            if(head==NULL)
            {  head=temp;
                x=head;
            }
            else
            { x->next=temp;
            x=x->next;
            }
            t2=t2->next;
        }
    
       
        
        if(carry>0)
        {
            temp=new ListNode(carry);
            x->next=temp;
        }
        
       
      


 

      return head;  
    }
};