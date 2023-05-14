function solution(my_string, indices) {
    let arr = [...my_string]
    for(let i=0;i<arr.length;i++){
        if(indices.includes(i)){
            arr[i]= 0
        } 
    }
    let answer = arr.filter(e => e!==0).join("")
    
    return answer;
}