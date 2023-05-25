function solution(s){
    let str = s.toLowerCase()
    let p = 0;
    let y = 0;
    for(let i of str){
        if(i==="p") p++
        if(i==="y") y++
    }
    return p===y ? true : false;
}