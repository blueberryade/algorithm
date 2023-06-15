function solution(s) {
    s = s.split(" ").map(e=> Number(e))
    return Math.min(...s)+' '+Math.max(...s);
}