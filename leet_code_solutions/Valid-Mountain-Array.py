class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        if (A.size()<3)
            return false;
        int flag = 0;
        int left=0;
        for (int i = 0 ; i< A.size()-1 ; i++)
        {
            if (flag==0 and A[i]<A[i+1])
            {left = 1;
                continue;
            }
            else if (flag==0 and A[i]>A[i+1])
                flag=1;
            else if (flag==1 and A[i]>A[i+1])  
                continue;
            else
                return false;
        }
        if (flag==1 and left==1)
        return true;
        else 
            return false;
    }
};