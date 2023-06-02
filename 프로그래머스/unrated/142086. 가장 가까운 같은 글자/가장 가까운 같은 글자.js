function solution(s) {
    var answer = [];
    let index = {};
    [...s].map((e,i) =>{
        if(e in index){
            answer.push(i-index[e][index[e].length-1])
            index[e].push(i);
            
        } else{
            index[e]=[i]
            answer.push(-1)
        }
    } )
    return answer;
}