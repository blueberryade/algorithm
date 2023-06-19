function solution(keymap, targets) {
    var answer = [];
    for(let i = 0;i<targets.length;i++){
        let temp = targets[i];
        let count = 0;
        for(let j=0;j<temp.length;j++){
            let str = temp[j];
            let min = Math.min(...keymap.map(e=>{
                let index = e.indexOf(str);
                return index === -1 ? Infinity : index+1;
            }))
            if(min === Infinity){
                count = -1;
                break
            }
            count +=min;
        }
        answer[i] = count
    }
    return answer;
}