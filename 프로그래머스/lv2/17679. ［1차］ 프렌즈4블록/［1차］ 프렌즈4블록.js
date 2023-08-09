function solution(m, n, board) {
    board = board.map(e=>e.split(""))
    
    while(true){
        const find = [];
        for(let i=0; i < m-1;i++){
            for(let j=0;j< n-1;j++){
                if(board[i][j]&&
                  board[i][j]===board[i][j+1]&&
                  board[i][j]===board[i+1][j]&&
                  board[i][j]===board[i+1][j+1]){
                    find.push([i,j])
                }
            }
        }
        if(!find.length) return board.flat().filter(e=>!e).length;
        
        find.forEach(([i,j])=>{
            board[i][j] = 0;
            board[i][j+1] = 0;
            board[i+1][j] = 0;
            board[i+1][j+1] = 0;
        })
        
        for(let i = m-1;i>=0;i--){
            for(let j=0;j<n;j++){
                for(let k = i-1;k>=0;k--){
                    if(board[i][j]) break
                    if(board[k][j]){
                        board[i][j] = board[k][j]
                        board[k][j] = 0;
                        break
                    }
                }
            }
        }
    }
}