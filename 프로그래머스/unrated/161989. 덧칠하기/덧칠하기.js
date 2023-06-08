function solution(n, m, section) {
    var answer = 0;
    let paint = 0;
    section.forEach(e=>{
        if(e>paint){
            answer++
            paint = e+m-1
        }
    })
    return answer;
}