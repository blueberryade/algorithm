function solution(left, right) {
    var answer = 0;
    for(let i=left;i<=right;i++){
        let sum  = 0
        for(let j=1;j<=i;j++){
            if(i%j===0) sum++
        }
        sum%2===0 ? answer+=i :  answer-=i
    }
    return answer;
}