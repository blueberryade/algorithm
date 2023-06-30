function solution(k, tangerine) {
    var answer = 0;
    const obj = {};
    tangerine.forEach((e) => obj[e] = (obj[e] || 0)+1);
    const arr = Object.values(obj).sort((a,b)=>b-a)
    for(let i of arr){
        answer++
        if(k>i) k-=i
        else break
    }
    return answer;
}