function solution(num_list) {
    var answer = 0;
    if(num_list.length>=11){
        for(let i of num_list){
            answer += i
        }
    } else {
        answer = num_list.reduce((a,b)=> a*b)
    }
    return answer  
}