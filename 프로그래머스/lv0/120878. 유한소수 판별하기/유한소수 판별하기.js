function solution(a, b) {
    function greatest(a,b) {
        if(b===0) return a;
        return greatest(b, a%b)
    }
    let d = b /greatest(a,b)
    while(d%2===0){
        d = d/2
    }
    while(d%5===0){
        d = d/5
    }
    return d===1 ? 1 : 2;
}