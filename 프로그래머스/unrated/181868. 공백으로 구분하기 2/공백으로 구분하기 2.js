function solution(my_string) {
    var answer = [];
    let arr = my_string.split(" ")
    for(let i of arr){
        if(i!=="") answer.push(i)
    }
    return answer;
}