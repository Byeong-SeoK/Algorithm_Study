#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;

    if(arr.size() == 1){
        answer.push_back(-1);
    }
    else{
        int num = arr[0];
        int index = 0;
        for(int i = 0; i < arr.size(); i++){
            if(num < arr[i]){
                continue;
            }
            else{
                num = arr[i];
                index = i;
            }
        }

        arr.erase(arr.begin() + index);
        answer.insert(answer.end(), arr.begin(), arr.end());
    }

    return answer;
}
