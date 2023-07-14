function solution(progresses, speeds) {
    var answer = [];
    let day = progresses.map((e,i)=>Math.ceil((100-e)/speeds[i]));
    let s = day[0];
    let count = 1;
    for(let i=1;i<day.length;i++){
        if(day[i]<=s){
            count++
        } else{
            s = day[i];
            answer.push(count)
            count = 1;
        }
    }
    answer.push(count)
    
    return answer;
}