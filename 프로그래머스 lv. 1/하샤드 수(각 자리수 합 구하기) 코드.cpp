bool solution(int x) {
    bool answer = true;

    int sum = 0;
    int n = x;
    while(n){
        int num = n % 10;
        sum = sum + num;
        
        n = n / 10;
    }

    if (x % sum == 0) {
        answer = true;
    }
    else {
        answer = false;
    }

    return answer;
}
