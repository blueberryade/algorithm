function solution(arr) {
    let answer = arr
    let a = arr.length
    let b = arr[0].length
    if(a===b) return arr
    if(a > b){
      return  arr.map(e=> e.concat([...Array(a-b).fill(0)]))
    } else {
       for(let i=0;i<b-a;i++){
           answer.push(Array(b).fill(0))
       }
        return answer
    }
}