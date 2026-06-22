class Solution {
public:
    int subarraySum(std::vector<int>& nums, int k) {
        int count = 0;
        int n = nums.size();
        for (int start = 0; start < n; ++start) {
            int current_sum = 0;
            for (int end = start; end < n; ++end) {
                current_sum += nums[end];
                if (current_sum == k) 
                    count++;
            }
        }
        return count;
    }
};
