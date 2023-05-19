function solution(myString) {
    var answer = [];
    myString.split("x").map(e=>answer.push(e.length))
    return answer;
}