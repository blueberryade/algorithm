function solution(number) {
    var answer = 0;
    let string = number.split("")
    for(let i of string){
        answer = answer +Number(i)
    }
    return answer%9;
}