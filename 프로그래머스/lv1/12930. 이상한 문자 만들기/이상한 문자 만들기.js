function solution(s) {
    var arr = s.split(" ");
    return arr.map(e=> e.split("").map((a,i)=> i%2===0 ? a.toUpperCase() : a.toLowerCase()).join("")).join(" ")

}