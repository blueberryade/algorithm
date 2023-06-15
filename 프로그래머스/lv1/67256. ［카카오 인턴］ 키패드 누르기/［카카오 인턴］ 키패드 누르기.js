function solution(numbers, hand) {
    function findkey(key){
        let keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]];
        for(let i=0;i<4;i++){
            for(let j=0;j<3;j++){
                if(keypad[i][j]===key){
                    return [i,j]
                }
            }
        }
    }
    var answer = '';
    let left = "*";
    let right = "#";
    for(let i of numbers){
        if(i === 1|| i === 4 || i ===7 ){
            answer+="L";
            left = i
        } else if(i === 3 || i ===6 || i ===9){
            answer+="R"
            right = i -2
        } else{
            let r = findkey(right);
            let l = findkey(left);
            let mid = findkey(i);
            let rd = Math.abs(r[0]-mid[0])+Math.abs(r[1]-mid[1]);
            let ld = Math.abs(l[0]-mid[0])+Math.abs(l[1]-mid[1]);
            if(rd === ld){
                hand === "right" ? (right=i,answer+="R") : (left=i,answer+="L")
            } else if(rd>ld){
                answer+="L"
                left = i;
            } else{
                answer+="R"
                right = i
            }
        }
    }
    
    return answer;
}