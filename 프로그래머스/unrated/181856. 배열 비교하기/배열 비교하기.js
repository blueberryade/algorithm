function solution(arr1, arr2) {
    if(arr1.length===arr2.length){
        let sum1 = arr1.reduce((acc,cur)=> acc+cur)
        let sum2 = arr2.reduce((acc,cur)=> acc+cur)
        return sum1===sum2 ? 0 : sum1>sum2 ? 1 : -1
    }
    return arr1.length > arr2.length ? 1 : -1;
}