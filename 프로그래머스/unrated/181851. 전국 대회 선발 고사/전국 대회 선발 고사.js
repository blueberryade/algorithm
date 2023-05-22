function solution(rank, attendance) {
    const [a,b,c]= rank.filter((e,i)=> attendance[i]).sort((a,b)=>a-b).map(e => rank.indexOf(e))
    return 10000 * a + 100 * b + c
}