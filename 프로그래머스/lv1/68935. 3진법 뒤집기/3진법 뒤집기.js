function solution(n) {
    var str = n.toString(3).split("").reverse().join("");
    return parseInt(str,3);
}


