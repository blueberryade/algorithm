function solution(id_list, report, k) {
    report = [...new Set(report)]
    var answer = Array(id_list.length).fill(0);
    let id = {};
    
    id_list.forEach(e=>{
        id[e]=[]
    })
    report.forEach(e=>{
        const [user,r] = e.split(" ");    
        id[r].push(user)
    })
    for(let key in id){
        if(id[key].length>=k){
            id[key].forEach(e=>answer[id_list.indexOf(e)]++)
        }
    }
    return answer;
}