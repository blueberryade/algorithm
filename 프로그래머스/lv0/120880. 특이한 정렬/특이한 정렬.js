function solution(numlist, n) {
    var answer = numlist.sort((a,b)=>
                              Math.abs(a-n)===Math.abs(b-n) ?
                              b-a : Math.abs(a-n)-Math.abs(b-n));
  
    return answer;
}