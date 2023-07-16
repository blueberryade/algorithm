function solution(str1, str2) {
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    let one = [];
    let two = [];
    for(let i=0;i<str1.length-1;i++){
        let str = str1.slice(i,i+2)
        if(str.replace(/[a-z]/g,'').length===0) one.push(str);
    }
    for(let i=0;i<str2.length-1;i++){
        let str =str2.slice(i,i+2);
        if(str.replace(/[a-z]/g,'').length===0) two.push(str);
    }
    if(one.length===0 && two.length===0) return 65536;
    let union = 0;
    let intersection = 0;
    let set = new Set([...one,...two])
    set.forEach(e=>{
        const has1 = one.filter(x=> x===e).length;
        const has2 = two.filter(x=> x===e).length;
        union+=Math.max(has1,has2);
        intersection +=Math.min(has1,has2);
    })
    return union === 0 ? 65536 : Math.floor(intersection/union*65536)
}