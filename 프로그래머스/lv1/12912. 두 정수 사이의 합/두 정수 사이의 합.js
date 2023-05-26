function solution(a, b) {
    var answer = 0;
    if(a<b){
    for(let i=a;i<=b;i++){
        answer+=i
    }
    } else {
        for(let j=b;j<=a;j++){
            answer+=j
        }
    }
    return answer;
}