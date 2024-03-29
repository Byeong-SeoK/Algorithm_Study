#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> temp = lost;
    vector<int> num(n, 1);//각 학생이 가지고 있는 체육복의 갯수를 1개로 저장한 벡터

    temp.insert(temp.end(), reserve.begin(), reserve.end());
    //temp는 예시 1번을 보면 [2,4,1,3,5] 형태를 갖게 된다.

    for (int i = 0; i < temp.size(); i++) {
        if (i < lost.size()) {
            num[temp[i] - 1] = 0;
        }
        else {
            if (num[temp[i] - 1] == 0) {
                num[temp[i] - 1] = 1;
            }
            else {
                num[temp[i] - 1] = 2;
            }
        }
    }
    //num에 저장된 값들을 0이나 2로 바꾸어 저장

    for (int k = 0; k < num.size(); k++) {
        if (k == 0) {//제일 처음 학생
            if (num[k] == 2) {
                if (num[k + 1] == 0) {
                    num[k] = num[k] - 1;
                    num[k + 1] = num[k + 1] + 1;
                    continue;
                }
                else {
                    continue;
                }
            }
            else {
                continue;
            }
        }
        else if (k == num.size() - 1) {//제일 마지막 학생
            if (num[k - 1] == 0) {
                num[k] = num[k] - 1;
                num[k - 1] = num[k - 1] + 1;
                continue;
            }
            else {
                continue;
            }
        }
        else {//첫번째와 마지막 학생 사이의 번호의 학생들
            if (num[k] == 2) {
                /*밑의 조건문에서 왼쪽의 학생부터 체육복을 주어야 최댓값이 나온다.*/
                if (num[k - 1] == 0) {
                    num[k] = num[k] - 1;
                    num[k - 1] = num[k - 1] + 1;
                    continue;
                }
                else if (num[k + 1] == 0) {
                    num[k] = num[k] - 1;
                    num[k + 1] = num[k + 1] + 1;
                    continue;
                }
                else {
                    continue;
                }
            }
            else {
                continue;
            }
        }
    }

    for (int j = 0; j < num.size(); j++) {
        if (num[j] > 0) {
            answer++;
        }
    }


    return answer;
}
