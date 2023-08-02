function solution(files) {
    var answer = [];
    files.forEach(file=>{
        const parts = ['','',''];
        [...file].forEach(word=>{
            const isNumber = !isNaN(parseInt(word));
            if(!isNumber && !parts[1].length){
                parts[0] +=word
            } else if(isNumber && !parts[2].length){
                parts[1] +=word
            } else{
                parts[2] +=word
            }
        })
        answer.push(parts)
    })
    answer.sort((a,b)=>{
        const stringA = a[0].toUpperCase()
        const stringB = b[0].toUpperCase()
        if(stringA > stringB){
            return 1;
        } else if(stringA < stringB){
            return -1;
        } else{
            const intA = parseInt(a[1])
            const intB = parseInt(b[1])
            return intA-intB
        }
    })
    return answer.map(arr=>arr.join(''));
}