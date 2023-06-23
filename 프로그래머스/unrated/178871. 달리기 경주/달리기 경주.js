function solution(players, callings) {
    let index = {};
    players.forEach((e,i)=>index[e]=i)
    callings.forEach((e,i)=>{
        let call = index[e]
        let temp = players[call-1]
        players[call-1] = players[call];
        players[call] = temp;
        index[e]--
        index[temp]++
    })
    return players;
}