function solution(n, lost, reserve) {
    var answer = n-lost.length;
    let realLost=lost.filter((e)=>!reserve.includes(e));
    let realReserve=reserve.filter((e)=>!lost.includes(e));
    answer+=lost.length-realLost.length;
    
    realLost.sort((a,b)=>a-b);
    
    realLost.forEach((e)=>{
        if(realReserve.length===0){
            return;
        }
        
        if(realReserve.includes(e-1)){
            realReserve=realReserve.filter((a)=>a!==e-1);
            answer++;
        }
        else if(realReserve.includes(e+1)){
            realReserve=realReserve.filter((a)=>a!==e+1);
            answer++;
        }
        
    })
    return answer;
}