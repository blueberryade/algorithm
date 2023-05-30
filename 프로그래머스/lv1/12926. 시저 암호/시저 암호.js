function solution(s, n) {
    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lower = "abcdefghijklmnopqrstuvwxyz";
    var answer = '';
    for(let i=0;i<s.length;i++){
        let string = s[i]
        if(string===" ") {
            answer+=" "
            continue
        }
        let li = upper.includes(string) ? upper : lower;
        let index = li.indexOf(string)+n;
        if(index >= upper.length) index -= upper.length;
        answer+= li[index]
        
    }
    return answer;
}