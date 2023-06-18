function solution(n, words) {
    for(let i=0;i<words.length;i++){
        let word = words[i];
        let num = i%n+1
        let turn = Math.floor(i/n)+1
        if(i>0){
            let last = words[i-1].split("").pop();
            if(i>words.indexOf(word) || words[i][0]!==last){
                return [num,turn]
            }
        }
    }
    return [0,0];
}