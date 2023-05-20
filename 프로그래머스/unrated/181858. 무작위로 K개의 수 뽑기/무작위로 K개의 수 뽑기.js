function solution(arr, k) {
    let set = new Set(arr)
    var answer = [...set];
    if(answer.length>=k) {
        return answer.slice(0,k)
    } else {
        while(answer.length<k){
        answer.push(-1)
        }
    }
    return answer
}