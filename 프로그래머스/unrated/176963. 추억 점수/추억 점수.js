function solution(name, yearning, photo) {
    var answer = [];
    photo.map(e =>{
        let sum = 0;
        e.map(a=>{
            let index = name.indexOf(a)
            if(index!==-1) sum+=yearning[index]
        })
        answer.push(sum)
    })
    return answer;
}