function solution(n_str) {
    if(n_str[0]!=="0"){
        return n_str
    } else {
        for(let i=0;i<n_str.length;i++){
            if(n_str[i]!=="0"){
                return n_str.slice(i)
            }
        }
    }
}