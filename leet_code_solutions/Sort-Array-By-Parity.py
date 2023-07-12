class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        
        int i = 0;
        int n = nums.size();
        int count = n;
        int k;
        while(i < count)
        {
            if(nums[i]%2 != 0)
            {
                k=nums[i];
                nums.erase(nums.begin()+i);
                count--;
                nums.push_back(k);
            }
            else
                i++;
                
            
        }
        return nums;
        
        
    }
};