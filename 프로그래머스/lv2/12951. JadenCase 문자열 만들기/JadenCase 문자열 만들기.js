function solution(s) {
    var answer = s.toLowerCase().split(" ").map(e=> e.charAt(0).toUpperCase()+e.slice(1)).join(" ")
    return answer;
}