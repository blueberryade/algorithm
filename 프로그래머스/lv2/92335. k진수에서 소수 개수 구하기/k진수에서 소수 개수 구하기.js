function solution(n, k) {
     function isPrime(number){
        if(number<=1){
            return false;
        }
        for(let i=2;i<=Math.sqrt(number);i++){
            if(number%i===0) return false
        }
        return true;
    }
    
    var answer = 0;
    let num = n.toString(k);
    let arr = num.split("0");
    for(let i=0;i<arr.length;i++){
        if(isPrime(+arr[i])) answer++
    }
    return answer;
}