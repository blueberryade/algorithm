function solution(my_string, queries) {
    for(let i of queries){
        let string = [...my_string.slice(i[0],i[1]+1)].reverse().join("")
        my_string = my_string.slice(0,i[0]) + string + my_string.slice(i[1]+1)
    }
    return my_string
}