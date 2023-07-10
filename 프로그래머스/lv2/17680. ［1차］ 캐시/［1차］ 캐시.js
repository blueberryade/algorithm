function solution(cacheSize, cities) {
    var answer = 0;
    let arr = [];
    for(let i=0;i<cities.length;i++){
        let cur = cities[i].toLowerCase();
        let findCity = arr.find(e=>e===cur)
        if(!findCity){
            arr.push(cur);
            if(arr.length>cacheSize){
                arr.shift()
            }
            answer+=5;
        } else{
            arr = arr.filter(e=>e!==cur)
            arr.push(cur)
            answer+=1
        }
    }
    return answer;
}