function solution(arr, idx) {
    for(let i=idx;i<arr.length;i++){
        var answer = i;
        if(arr[i]===1) return answer
    }
    return -1;
}