function solution(dartResult) {
    var answer = [];
    let temp = 0;
    let dart = dartResult.split("")
    for(let i =0;i<dart.length;i++){
        if(!isNaN(dart[i])){
            if(dart[i]==="1" && dart[i+1]==="0"){
                temp = 10;
                i++
            } else{
                temp = +dart[i]
            }
        }
        if(dart[i]==="S") answer.push(temp)
        if(dart[i]==="D") answer.push(Math.pow(temp,2))
        if(dart[i]==="T") answer.push(Math.pow(temp,3))
        if(dart[i]==="#") answer[answer.length-1] *=-1
        if(dart[i]==="*"){
            answer[answer.length-1]*=2;
            answer[answer.length-2]*=2;
        }
    }
    return answer.reduce((a,c)=> a+c)
}