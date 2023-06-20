function solution(new_id) {
    let id = new_id
    .toLowerCase()
    .replace(/[^\w\-\.]/g,"")
    .replace(/\.{2,}/g,".")
    .replace(/^\.|\.$/g,"")
    .replace(/^$/,"a")
    .slice(0,15)
    .replace(/\.$/,"")
    let len = id.length;
    if(len<=2) id = id+id[len-1].repeat(3-len)
    return id;
}