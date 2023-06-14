function solution(board, moves) {
    let doll = []
    var answer = 0;
    moves.forEach(e=>{
        for(let i=0;i<board.length;i++){
            if(board[i][e-1]!==0){
                if(doll[doll.length-1]===board[i][e-1]){
                    doll.pop()
                    answer+=2
                } else{
                    doll.push(board[i][e-1])
                }
                board[i][e-1]=0
                break
            }
        }
        
    })
    return answer;
}