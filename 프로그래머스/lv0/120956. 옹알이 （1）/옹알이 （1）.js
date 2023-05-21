function solution(babbling) {
    var answer = 0;
    return babbling.map(e => e.replace(/aya|ye|woo|ma/g,"")).filter(e => !e).length
    
}