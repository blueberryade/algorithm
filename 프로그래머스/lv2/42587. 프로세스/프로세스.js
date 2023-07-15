function solution(priorities, location) {
    var answer = 0;
    let max = Math.max(...priorities);
    let arr = [];
    for(let i=0;i<priorities.length;i++){
        arr.push(i)
    }
    while(priorities.length!==0){
        max = Math.max(...priorities)
        if(priorities[0]<max){
            priorities.push(priorities.shift())
            arr.push(arr.shift())
        } else{
            answer+=1;
            priorities.shift();
            if(arr.shift()==location){
                return answer
            }
        }
    }

}