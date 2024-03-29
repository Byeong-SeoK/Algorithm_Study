#include <string>
#include <vector>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int size = priorities.size();

    while (size != 0) {
        bool find = false;
        int max = priorities[0];

        for (int i = 0; i < priorities.size(); i++) {
            if (max < priorities[i]) {
                find = true;
                break;
            }
        }

        if (find) {
            priorities.push_back(max);
            priorities.erase(priorities.begin());

            if (location > 0) {
                location--;
            }
            else {
                location = priorities.size() - 1;
            }
        }
        else {
            priorities.erase(priorities.begin());

            if (location == 0) {
                answer++;
                break;
            }
            else {
                location--;
                answer++;
            }
        }

        size = priorities.size();
    }

    return answer;
}
