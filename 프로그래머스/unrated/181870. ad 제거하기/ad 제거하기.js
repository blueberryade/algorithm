function solution(strArr) {
    var answer = [];
    strArr.forEach(e => !e.includes("ad") ? answer.push(e) : "")
    return answer;
}