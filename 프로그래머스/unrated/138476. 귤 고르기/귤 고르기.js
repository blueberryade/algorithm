function solution(k, tangerine) {
    var answer = 0;
    let count = {};
    tangerine.forEach(e=> e in count ? count[e]++ : count[e]=1)
    let sort = Object.values(count).sort((a,b)=>b-a);
    let sum = 0;
    for(let i of sort){
        answer++
        sum+=i
        if(sum>=k) break
    }
    return answer;
}

