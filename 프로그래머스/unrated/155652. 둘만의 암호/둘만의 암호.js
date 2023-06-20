function solution(s, skip, index) {
    var answer = '';
    let alphabet ='abcdefghijklmnopqrstuvwxyz'.split("")
    let skipArr = alphabet.filter(e=>!skip.includes(e))
    for(let i of s){
        answer+= skipArr[(skipArr.indexOf(i)+index)%skipArr.length]
    }
    return answer;
}