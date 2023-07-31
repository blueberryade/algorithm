function solution(n) {
    var answer = '';
    const num = [4,1,2]
    while(n){
        answer = num[n%3] + answer
        n = Math.floor((n-1)/3)
    }
    return answer;
}