function solution(binomial) {
    const[a,o,b] =binomial.split(" ")
    if(o==="*"){
        return +a * +b
    } else if(o==="+"){
        return +a + +b
    } else{
        return  +a - +b
    }
    
}