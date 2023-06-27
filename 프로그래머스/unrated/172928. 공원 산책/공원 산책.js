function solution(park, routes) {
    let pos = [0,0]
    const dict = {
        E:[0,1],
        W:[0,-1],
        S:[1,0],
        N:[-1,0]
    }
    for(let i=0;i<park.length;i++){
        let findIdx = park[i].indexOf("S");
        if(findIdx>-1){
            pos = [i,findIdx]
            break;
        }
    }
    routes.forEach((e,i)=>{
        let [p,range] = e.split(" ");
        let temp = [...pos];
        let n = false;
        for(let i=0;i<range;i++){
            temp[0]+=dict[p][0];
            temp[1]+=dict[p][1];
            
            if((temp[0]<0)||(temp[0]>park.length-1)||(temp[1]<0)||(temp[1]>park[0].length-1)){
                n = true;
                break
            }
            if(park[temp[0]][temp[1]]==='X'){
                n = true;
                break
            }
        }
        if(!n){
            pos = temp
        }
    })
    return pos;
}