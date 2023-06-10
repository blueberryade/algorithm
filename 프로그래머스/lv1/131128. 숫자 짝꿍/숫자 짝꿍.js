function solution(X, Y) {
    var answer = '';
    let x = X.split("")
    let y = Y.split("")
    for(let i=0;i<10;i++){
        let tempX = x.filter(e => Number(e)===i).length
        let tempY = y.filter(e=> Number(e)===i).length
        answer+= String(i).repeat(Math.min(tempX,tempY))
    }
    if(answer.length===0) return "-1"
    if(Number(answer)===0) return "0"
    return answer.split("").sort((a,b)=>Number(b)-Number(a)).join("");
}