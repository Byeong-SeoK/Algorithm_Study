#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> buckets;

    int move = 0;
    for (int i = 0; i < moves.size(); i++) {
        move = moves[i] - 1;

        for (int j = 0; j < board.size(); j++) {
            if (board[j][move] != 0) {
                buckets.push_back(board[j][move]);
                board[j][move] = 0;
                break;
            }
        }

        int size = buckets.size();
        for (int k = 0; k < size - 1; k++) {
            if (buckets[k] == buckets[k + 1]) {
                buckets.erase(buckets.begin() + k, buckets.begin() + k + 2);
                answer = answer + 2;
                size = buckets.size(); 
	   //board벡터가 전부다 1일때 size값이 바뀌므로 새로이 size값을 정의해야 한다.
                //만약 size값을 바꾸지 않으면 k = 1인데 벡터 길이는 0인 벡터 범위를 벗어난 경우가 생긴다.
	}
        }
    }

    return answer;
}
