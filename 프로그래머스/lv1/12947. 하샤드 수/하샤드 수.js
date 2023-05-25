function solution(x) {
    let num = 0
    x.toString().split("").forEach(e=> num+=Number(e))
    return x%num===0 ? true : false;
}