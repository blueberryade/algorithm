function solution(myString, pat) {
    var answer = "";
    for(let i of myString){
        if(i==="A") answer+="B"
        if(i==="B") answer+="A"
    }
    
    return answer.includes(pat) ? 1 : 0;
}