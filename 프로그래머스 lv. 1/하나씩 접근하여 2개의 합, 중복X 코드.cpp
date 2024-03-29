#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;

    for (int i = 0; i < numbers.size() - 1; i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            int num = numbers[i] + numbers[j];

            if (answer.size() == 0) {
                answer.push_back(num);
            }
            else {
                bool find = false;
                for (int k = 0; k < answer.size(); k++) {
                    if (answer[k] == num) {
                        find = true;
                        break;
                    }
                }

                if (!find) {
                    answer.push_back(num);
                }
            }
        }
    }

    sort(answer.begin(), answer.end());

    return answer;
}
