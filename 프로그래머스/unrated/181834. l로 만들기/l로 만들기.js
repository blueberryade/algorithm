function solution(myString) {
    var answer = '';
    const alpha = ["a","b","c","d","e","f","g","h","i","j","k"]
    for(let i of myString){
        if(alpha.includes(i)){
            answer+="l"
        } else{
             answer+=i
        }
    }
    return answer;
}