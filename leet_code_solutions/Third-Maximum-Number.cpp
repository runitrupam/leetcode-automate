class Solution {
public:
    int thirdMax(vector<int>& A) {
        sort(A.begin(),A.end());
        auto it = unique(A.begin(),A.end());
        A.resize(std::distance(A.begin(), it));
        if(A.size()>=3)
            return A[A.size()-3];
        else
            return A[A.size()-1];
    }
};