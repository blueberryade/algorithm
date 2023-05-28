function solution(s) {
    if((s.length===4 || s.length===6) && [...s].filter(e=> isNaN(e)).length===0){
        return true
    } else{
        return false
    }
}