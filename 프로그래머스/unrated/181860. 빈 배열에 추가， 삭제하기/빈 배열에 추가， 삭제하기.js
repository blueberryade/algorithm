function solution(arr, flag) {
    var answer = [];
    arr.map((e,i)=>{
        flag[i] ? answer = answer.concat(Array(e*2).fill(e)) : answer.splice(answer.length-e)
    })
    return answer;
}