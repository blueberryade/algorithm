function solution(strArr) {
    var answer = {};
    for(let i of strArr){
        i.length in answer ? answer[i.length] : answer[i.length] =[]
        answer[i.length].push(i)
    }
    return Math.max(...Object.values(answer).map(e=>e.length))
}