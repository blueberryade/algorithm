function solution(a, b, c, d) {
    let arr = [a,b,c,d].sort();
    const [...set] = new Set(arr)
    const[p,...rest] = new Set(arr)
    if(set.length===1) return 1111*set[0];
    if(set.length===4) return Math.min(...arr);
  
    if(set.length===2){
        if(arr.filter(e=>e===p).length===2){
            return  (p+rest[0]) * Math.abs(p-rest[0])
        } else{
            return arr.filter(e=>e===p).length===1 ? (10*rest[0]+p) ** 2 : (10*p+rest[0]) **2
        }
    }
    if(set.length===3){
        let index = 0;
        let result = 1;
        for(let i of set){
            if(arr.filter(e=>e===i).length===2) index+=i
        }
        for(let e of set){
            if(e!==index){
                result *= e
            }
        }
        return result
    }
    }
    
