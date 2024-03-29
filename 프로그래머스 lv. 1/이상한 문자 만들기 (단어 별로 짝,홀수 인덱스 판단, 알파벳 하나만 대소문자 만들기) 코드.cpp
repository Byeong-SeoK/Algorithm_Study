#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    
    string temp = ""; //answer로 넘겨주기전 잠시 거쳐가는 변수
    
    //밑의 for문에서는 공백을 기준으로 단어를 잘라서 각 단어를 내부의 for문에서 다룸
    for(int i = 0; i < s.size(); i++){
        if(s[i] == ' '){
            temp = temp + s[i];
            
            for(int j = 0; j < temp.size(); j++){ //한 단어의 짝수번째 알파벳을 대문자로 만듬
                if(j % 2 == 0){
                    temp[j] = toupper(temp[j]);
                }
                else{
                    temp[j] = tolower(temp[j]);
                }
            }
            
            answer = answer + temp;
            temp = "";
        }
        else{
            temp = temp + s[i];
        }
    }
    
    //밑의 for문에서 인수로 받은 문장의 마지막 단어 다루기
    for(int k = 0; k < temp.size(); k++){
        if(k % 2 == 0){
            temp[k] = toupper(temp[k]);
        }
        else{
            temp[k] = tolower(temp[k]);
        }
    }
    
    answer = answer + temp;
    
    return answer;
