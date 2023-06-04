function solution(k, score) {
    var answer = [];
    for(let i=1;i<=score.length;i++){
        let arr = score.slice(0,i).sort((a,b)=>b-a);
        i<k+1 ? answer.push(Math.min(...arr)) : answer.push(arr[k-1])
    }
    return answer;
}