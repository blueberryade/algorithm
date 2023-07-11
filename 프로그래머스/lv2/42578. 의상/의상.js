function solution(clothes) {
    var answer = 1;
    let map = {};
    clothes.forEach(e=>{
        const [type,name] = e;
        name in map ? map[name]++ : map[name]=1
    })
    for(let key in map){
        answer *=(map[key]+1)
    }
    return answer-1;
}