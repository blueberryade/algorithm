function solution(arr) {
    let min = 1;
    while(min<arr.length){
        min = min*2
    }
    return [...arr,...Array(min-arr.length).fill(0)];
}


