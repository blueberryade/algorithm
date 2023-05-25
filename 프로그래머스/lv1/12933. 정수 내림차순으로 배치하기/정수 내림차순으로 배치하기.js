function solution(n) {
    return Number(n.toString().split("").map(e => +e).sort((a,b)=> b-a).join(""));
}