function solution(n) {
    let arr = Array.from(Array(n), () => Array(n).fill(0))
    let num = 1;
    let rowS = 0;
    let colS = 0;
    let rowE = n-1;
    let colE = n-1;
    while(rowS<=rowE && colS<=colE){
        for(let i=colS;i<=colE;i++){
            arr[colS][i]=num++
        }
        rowS++
        for(let i=rowS;i<=rowE;i++){
            arr[i][colE]=num++
        }
        colE--
        for(let i=colE;i>=colS;i--){
            arr[rowE][i]=num++
        }
        rowE--
        for(let i=rowE;i>=rowS;i--){
            arr[i][colS]=num++
        }
        colS++
    }
    return arr;
}