function solution(s) {
    let str = s.split("");
    var answer = 0;
    let xCount = 1;
    let yCount = 0;
    let index = 1;
    while(str.length>0){
        let first = str[0];
        if(first === str[index]){
            xCount++
        } else {
            yCount++
        }
        if(xCount !== yCount){
            index++
        } else {
            answer++;
            str.splice(0,index+1);
            xCount =1;
            yCount =0;
            index = 1;
        }
    }
    return answer;
}