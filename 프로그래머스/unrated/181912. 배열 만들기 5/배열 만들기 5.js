function solution(intStrs, k, s, l) {
    var answer = [];
    intStrs.forEach(e => {
        let string = e.slice(s,s+l)
        if(Number(string)>k) answer.push(Number(string))
    })
    return answer;
}