function solution(arr, n) {
    if(arr.length%2===0){
        return arr.map((e,i) => 
            i%2!==0 ? e+n : e
        )
    } else{
        return arr.map((e,i)=>
                      i%2===0 ? e+n : e)
    }
  

}