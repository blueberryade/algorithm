function solution(my_string) {
    var answer = Array(52).fill(0);
    let arr1 = Array(26).fill().map((v, i) => String.fromCharCode(i + 65));
    let arr2 = Array(26).fill().map((v, i) => String.fromCharCode(i + 97));
    let alpha =[...arr1,...arr2]
    for(let i=0;i<my_string.length;i++){
        let index = alpha.indexOf(my_string[i])
        answer[index]++
    }
    return answer;
}