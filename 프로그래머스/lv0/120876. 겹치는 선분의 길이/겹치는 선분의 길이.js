function solution(lines) {
    var answer = 0;
    const [a,b,c] = lines;
    for(let i=-100;i<=100;i++){
        let cnt = 0
        if(a[0]<=i && i<a[1]) cnt++
        if(b[0]<=i && i<b[1]) cnt++
        if(c[0]<=i && i<c[1]) cnt++
        
        if(cnt>1) answer++
    }
    return answer;
}