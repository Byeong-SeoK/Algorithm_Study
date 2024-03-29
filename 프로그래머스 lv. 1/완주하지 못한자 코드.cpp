#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    sort(participant.begin(), participant.end());

    int start = 0;
    int end = participant.size();
    int num = 0;
    int len = completion.size();

    while (num < len) {
        int mid = (start + end) / 2;
        if (participant[mid] < completion[num]) {
            start = mid + 1;
        }
        else if (participant[mid] == completion[num]) {
            participant.erase(participant.begin() + mid);
            num++;
            start = 0;
            end = participant.size();
        }
        else {
            end = mid - 1;
        }
    }
    answer = participant[0];

    return answer;
}

int main() {
    vector<string> participant = { "marina", "josipa", "nikola", "vinko", "filipa" };
    vector<string> completion = { "josipa", "filipa", "marina", "nikola" };

    cout << solution(participant, completion);

    return 0;
}

위의 방식대로 짜면 걸리는 시간 복잡도는
sort함수에서의 O(nlogn)
while문에서 O(logn)^4 (왜냐하면 completion배열의 요소당 logn씩 걸리기 때문)
따라서 총 시간 복잡도는 O(nlogn) + O(logn)^4 = O(logn)^4 이렇게 된다.




string solution(vector<string> participant, vector<string> completion) { 
	sort(participant.begin(), participant.end());
	sort(completion.begin(), completion.end()); 

	for(int i = 0; i < completion.size(); ++i) { 
		if(participant[i] != completion[i]) { 
			return participant[i]; 
		}
	} 
	
	return participant[participant.size() - 1]; 
}

출처: https://boycoding.tistory.com/226 [소년코딩]

이렇게 짜면
sort에서 O(nlogn) 2번
for문에서 O(n)이 되어서
총 시간 복잡도는 O(nlogn) + O(nlogn) + O(n) = O(nlogn)이 된다.

따라서 위의 O(logn)^4 < O(logn) 이므로 밑의 코드가 효율성 면에서 훨씬 좋다
