function solution(n) {
    var answer = [];
    for(let i=0;i<n;i++){
        answer.push(Array(n).fill(0))
        for(let j=0;j<n;j++){
            if(i===j){
                answer[i][j]=1
            }
        }
    }
    return answer;
}