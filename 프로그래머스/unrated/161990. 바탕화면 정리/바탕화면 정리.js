function solution(wallpaper) {
    let lux = [];
    let luy = [];
    for(let i=0;i<wallpaper.length;i++){
        for(let j=0;j<wallpaper[i].length;j++){
            if(wallpaper[i][j]==="#"){
                lux.push(i)
                luy.push(j)
            }
        }
    }
    let minX = Math.min(...lux)
    let minY = Math.min(...luy)
    let maxX = Math.max(...lux)+1
    let maxY = Math.max(...luy)+1
    
    return [minX,minY,maxX,maxY];
}