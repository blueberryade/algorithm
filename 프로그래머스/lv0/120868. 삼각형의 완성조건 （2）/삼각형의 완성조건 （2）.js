function solution(sides) {
    var answer = 0;
    let max = Math.max(...sides)
    let min = Math.min(...sides)
    for(let i=max+1;i<max+min;i++){
        answer+=1
    }
    for(let i = max+1-min;i<=max;i++){
        answer+=1
    }
    return answer;
}