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
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head)
            return NULL;
        
        int count = 0;
        ListNode *temp = head;
        
        
        while(temp)
        {
            temp=temp->next;
            count++;
        }
        
        if(k%count == 0)
            return head;
        int rotate_times = k%count;
        
        int i = 1;
        temp = head;
         ListNode *y;  
        while(i <=(count - rotate_times))
        {
            if(i == (count - rotate_times) )
            {y = temp;
            temp = temp->next;
             y->next = NULL;
            }
            else
                temp=temp->next;
            i++;   
        }
        y = temp;
        while(temp->next != NULL)
        {
            temp=temp->next;
        }
        
        temp->next = head ;
        head = y;
        
        return head;
    }
};