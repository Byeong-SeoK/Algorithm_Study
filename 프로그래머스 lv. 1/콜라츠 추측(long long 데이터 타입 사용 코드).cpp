int solution(int num) {
    long long temp = num;
    int answer = 0;
    
    while(temp != 1){
        if(answer < 500){
            if(temp % 2 == 0){
                temp = temp / 2;
            }
            else{
                temp = temp * 3 + 1;
            }
            answer++;
        }
        else{
            return -1;
        }
    }
    return answer;
}
