class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int n = nums.size();
        int count = n;
        while(i < nums.size())
        {
            if(nums[i] == val)
            {
                count--;
                nums.erase(nums.begin()+i);
            }
            else
                i++;
            
        }
        return count;
    }
};