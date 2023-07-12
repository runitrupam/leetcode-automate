class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& A) {
        sort(A.begin(),A.end());
        int n = A.size();
        auto it = unique(A.begin(),A.end());
        A.resize(std::distance(A.begin(),it));
        
        vector <int> B;
        int j = 0;
        for(int i=1;i<=n;i++)
        {
            if(A[j]!=i)
                B.push_back(i);
            else
                j++;
        }
        
        
        return B;
    }
};