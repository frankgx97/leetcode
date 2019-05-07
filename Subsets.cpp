#include <vector>
using namespace std;
class Solution {
public:
    vector<int> candidates;
    vector<vector<int>> results;
    vector<vector<int>> subsets(vector<int> &nums) {
        candidates = nums;
        vector<int> empty_vector;
        dfs(0, empty_vector);
        return results;
        
    }
    void dfs(int index, vector<int> path){
        if (path.size() > candidates.size()){
            return;//backtrack
        }
        results.push_back(path);
        for (int i = index; i < candidates.size(); i++){
            vector<int> temp = path;
            temp.push_back(candidates[i]);
            dfs(i+1, temp);
        }   
    }
};
