function solution(arr) {
    var answer = arr.filter(e => e!==Math.min(...arr));
    return arr.length < 2 ? [-1] : answer;
}