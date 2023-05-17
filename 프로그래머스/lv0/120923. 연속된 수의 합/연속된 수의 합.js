function solution(num, total) {
    var answer = [];
    if(num%2!==0){
        const first = total / num - Math.floor(num/2)
        for(let i=first;i<first+num;i++){
            answer.push(i) 
        }
    }
        else {
            const first = Math.floor(total / num ) - (Math.floor(num/2)-1)
            for(let i=first;i<first+num;i++){
                answer.push(i)
            }
        }
         return answer;
    }
   
