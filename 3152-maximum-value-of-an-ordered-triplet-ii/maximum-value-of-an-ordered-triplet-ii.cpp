class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> pre(n+1);
        vector<int> suf(n+1);
        pre[0] = nums[0];
        for(int i=1; i<n; i++){
            pre[i] = max(pre[i-1], nums[i]);
        }
        suf[n-1] = nums[n-1];
        for(int i=n-2; i>=0; i--){
            suf[i] = max(suf[i+1], nums[i]);
        }
        long long ans = 0;
        for(int i=1; i<n-1; i++){
            long long val = (long long)(pre[i-1] - nums[i]) * suf[i+1];
            ans = max(ans, val);
        }
        return ans;
    }
};