function solution(lottos, win_nums) {
    let zero = lottos.filter(e=> e===0).length
    let match = lottos.filter(e=> win_nums.includes(e)).length
    let min = 7-match >=6 ? 6 : 7-match
    let max= min-zero < 1 ? 1: min-zero
    return [max,min];
}