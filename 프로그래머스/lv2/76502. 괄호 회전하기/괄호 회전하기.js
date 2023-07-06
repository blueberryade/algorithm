function solution(s) {
    if(s.length%2===1) return 0;
    var answer = 0;
    for(let i=0;i<s.length;i++){
        let temp = s.slice(i)+s.slice(0,i);
        let stack = [];
        let flag = true;
        for(let j of temp){
            if(j==="(" || j==="{" || j==="[") stack.push(j);
            else{
                let top = stack.pop();
                if(j===")" && top==="(") continue
                if(j==="}" && top==="{") continue
                if(j==="]" && top==="[") continue
                flag = false
                break
            }
        }
        if(flag) answer++
    }
    return answer;
}