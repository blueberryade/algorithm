function solution(arr, queries) {
    for(let i=0;i<queries.length;i++){
        const [from,to] = queries[i]
        for(let j=from;j<=to;j++){
            arr[j]+=1
        }
    }
    return arr
}