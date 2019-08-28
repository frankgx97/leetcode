#include <vector>

class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<int> memo;
        for(int i=0;i<nums.size();i++){
            memo.push_back(0);
        }
        memo[0] = 1;
        
        for(int i=0;i<nums.size();i++){
            if (memo[i] == 0){
                i++;
                continue;
            }else{
                for(int j=i;j<i+nums[i]+1;j++){
                    if(j>=nums.size()){
                        break;
                    }
                    memo[j] = 1;
                }
            }
        }
        if (memo[memo.size()-1]){
            return true;
        }else{
            return false;
        }   
    }
};
