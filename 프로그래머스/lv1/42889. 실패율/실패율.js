function solution(N, stages) {
    var answer = [];
    let len = stages.length
    for(let i=1;i<=N;i++){
        let stage = stages.filter(e => e===i).length;
        answer.push([i,stage/len])
        len = len - stage
    }
    answer.sort((a,b)=>b[1]-a[1])
    return answer.map(e=>e[0]);
}