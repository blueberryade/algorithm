function solution(spell, dic) {
    let string = spell.sort().join("");
    for(let i of dic){
        if(i.split("").sort().join("") === string){
            return 1
        } 
    }
    return 2
}