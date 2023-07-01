function solution(brown, yellow) {
    let total = brown+yellow
    for(let i=Math.floor(total/2);i>0;i--){
        if(total%i !== 0) continue;
        
        const width = i;
        const height = total/i;
        
        if((width-2)*(height-2)===yellow){
              return [width,height]
        }
      
    }
}