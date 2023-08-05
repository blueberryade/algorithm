function solution(numbers) {
    return numbers.map(e=>{
        let str = '0'+e.toString(2)
        if(str[str.length-1]==='0'){
            str = str.substring(0,str.length-1)+'1'
        } else{
            let idx = str.lastIndexOf('01')
            str = str.substring(0,idx) + '10' + str.substring(idx+2,str.length)
        }
        return parseInt(str,2)
    })
}