function solution(myString, pat) {
    var answer = '';
    for(let i = myString.length;i>=0;i--){
        let  arr = myString.slice(0,i)
        if(arr.endsWith(pat)) return answer +=arr
    }

}