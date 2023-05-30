function solution(sizes) {
    sizes.forEach((e,i)=> {
        sizes[i] = e.sort((a,b)=>a-b)
    } )
    const left = Math.max(...sizes.map(e=>e[0]))
    const right = Math.max(...sizes.map(e=>e[1]))
    return left*right;
}