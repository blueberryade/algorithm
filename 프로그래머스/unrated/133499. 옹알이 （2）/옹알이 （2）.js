function solution(babbling) {
    var answer = 0;
    const b = ["aya", "ye", "woo", "ma"];
    for(let i=0;i<babbling.length;i++){
        let babble = babbling[i];
        for(let j=0;j<b.length;j++){
           if(babble.includes(b[j].repeat(2))){
               break;
           } 
            babble = babble.split(b[j]).join(" ")
        }
        if(babble.split(" ").join("").length ===0){
            answer++
        }
    }
    return answer;
}