function solution(want, number, discount) {
    var answer = 0
    discount.forEach((e,i)=>{
        let arr = [...discount].slice(i,i+10);
        if(arr.length<10) return answer;
        
        let count= 0;
        for(let j=0;j<want.length;j++){
            if([...arr].filter(el=>el===want[j]).length===number[j]) count++
            else break
        }
        if(count===want.length) answer++
    })
    return answer;
}