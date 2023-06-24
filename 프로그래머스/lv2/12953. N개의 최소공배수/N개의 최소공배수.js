function solution(arr) {
    function greatest(a,b){
        if(b===0) return a;
        return greatest(b, a%b)
    }
    return arr.reduce((a,b)=> (a*b)/greatest(a,b))
}