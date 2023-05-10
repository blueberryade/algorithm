function solution(board) {
    const x = [1,0,-1,0,1,1,-1,-1]
    const y = [0,1,0,-1,1,-1,1,-1]
    const n = board.length
    var answer = n*n;
    const danger = [];
    for(let i=0;i<n;i++){
        for(let j=0;j<n;j++){
            if(board[i][j]===1){
                danger.push([i,j])
                answer--;
            }
        }
    }
    danger.forEach((e)=>{
        for(let k=0;k<8;k++){
            const nx = e[0]+x[k];
            const ny = e[1]+y[k];
            if(0<=nx && 0<=ny && nx < n && ny < n && board[nx][ny]===0){
                board[nx][ny] = 1
                answer--
            }
        }
    })
    return answer;
}