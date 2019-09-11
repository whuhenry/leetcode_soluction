#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result;
        result.resize(nums.size());
        result[0] = 1;
        
        for (int i = 1; i < nums.size(); ++i) {
            result[i] = result[i - 1] * nums[i - 1];       
        }

        int afterMul = nums[nums.size() - 1];

        for (int i = nums.size() - 2; i >= 0; --i) {
            result[i] *= afterMul;
            afterMul *= nums[i];
        }

        return result;
    }
};