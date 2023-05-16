function solution(str_list) {
    const idxl = str_list.indexOf("l")
    const idxr = str_list.indexOf("r");
    if(idxl===-1 && idxr!==-1) return str_list.slice(idxr+1)
    if(idxl!==-1 && idxr===-1) return str_list.slice(0,idxl)
    if(idxl===-1 && idxr===-1) return [];
    return idxl < idxr ?  str_list.slice(0,idxl) :  str_list.slice(idxr+1)
}