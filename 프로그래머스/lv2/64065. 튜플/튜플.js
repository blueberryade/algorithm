function solution(s) {
    var answer = [];
    let arr = [];
    s.slice(2,s.length-2).split("},{").forEach(e=>arr.push(e.split(',')))
    arr.sort((a,b)=>a.length-b.length)
    arr.forEach(e=>{
        e.forEach(a=>{
            if(!answer.includes(+a)) answer.push(+a)
        })
    })
    return answer;
}