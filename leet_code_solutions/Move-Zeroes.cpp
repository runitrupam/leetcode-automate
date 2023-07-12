class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int i = 0;
        int n = nums.size();
        int count = n;
        while(i < nums.size())
        {
            if(nums[i] == 0)
            {
                nums.erase(nums.begin()+i);
                count--;
            }
            else
                i++;
                
            
        }
        if (count<n)
            nums.insert(nums.end(),n-count,0);
        
        
    }
};