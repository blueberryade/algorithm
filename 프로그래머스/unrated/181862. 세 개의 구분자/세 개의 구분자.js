function solution(myStr) {
    var answer = myStr.split(/[a|b|c]/g).filter(e=>e)
    
    return answer.length ? answer : ["EMPTY"] ;
}