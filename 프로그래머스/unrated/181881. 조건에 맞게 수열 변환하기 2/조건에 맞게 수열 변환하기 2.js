function solution(arr) {
    var answer = 0;
    let prev = arr;
    
    while(true){
        const temp = prev.map(e=>{
            if(e>=50 && e%2===0) return e/2
            if(e<50 && e%2!==0) return e*2+1
            return e
        })
        if(prev.every((e,i)=> e=== temp[i])) break
        answer+=1
        prev = temp
        
    }
    return answer;
}