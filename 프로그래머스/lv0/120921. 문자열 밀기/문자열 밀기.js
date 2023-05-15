function solution(A, B) {
    var answer = 0;
    let a = [...A]
    let push = [A]
    for(let i=A.length-1;i>0;i--){
        push.push(a.slice(i).join("") + a.slice(0,i).join(""))
    }

    return push.includes(B) ? push.indexOf(B) : -1
  

  
}