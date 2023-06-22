function solution(survey, choices) {
    var answer = '';
    let type = {R:0,T:0,C:0,F:0,J:0,M:0,A:0,N:0}
    survey.forEach((e,i)=>{
        let score = Math.abs(choices[i]-4)
        if(choices[i]<4){
            type[e[0]]+=score
        } else if(choices[i]>4){
            type[e[1]]+=score
        }
    })
    const key = Object.keys(type)
    for(let i=0;i<key.length;i+=2){
        let left = type[key[i]]
        let right = type[key[i+1]]
        left >=right ? answer+=key[i] : answer+=key[i+1]
    }
    return answer;
}