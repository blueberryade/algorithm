function solution(my_string, m, c) {
    let arr = [];
    var answer = '';
    for(let i=0;i<my_string.length;i+=m){
        arr.push(my_string.slice(i,i+m))
    }
    for(let i=0;i<arr.length;i++){
        answer += arr[i][c-1]
    }
    return answer;
}