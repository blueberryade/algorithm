function solution(n) {
    var answer = String(n).split("").reverse().map(e => +e);
    return answer;
}