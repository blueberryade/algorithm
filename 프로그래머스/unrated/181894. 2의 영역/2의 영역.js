function solution(arr) {
    if(arr.indexOf(2)===-1) return [-1]
    const index1 = arr.indexOf(2)
    const index2 = arr.lastIndexOf(2)
    return arr.slice(index1,index2+1)
}