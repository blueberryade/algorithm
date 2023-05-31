function solution(n, arr1, arr2) {
    var answer = [];
    let map1 = arr1.map(e=> e.toString(2)).map(e=> e.length===n ? e :"0".repeat(n-e.length)+e)
    let map2 = arr2.map(e=> e.toString(2)).map(e=> e.length===n ? e :"0".repeat(n-e.length)+e)
    
    for(let i=0;i<n;i++){
        let str="";
        for(let j=0;j<n;j++){
            map1[i][j]==="0" && map2[i][j]==="0" ? str += " " : str +="#"  
        }
        answer.push(str)
    }
    return answer;
}