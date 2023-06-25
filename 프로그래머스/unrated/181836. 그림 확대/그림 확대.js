function solution(picture, k) {
    let arr1 = [];
    for(let i=0;i<picture.length;i++){
        let str = ""
        for(let j=0;j<picture[i].length;j++){
            for(let a =0;a<k;a++){
                str+=picture[i][j]
            }
        }
        arr1.push(str)
    }
    let answer = [];
    for(let i=0;i<arr1.length;i++){
        for(let j=0;j<k;j++){
             answer.push(arr1[i])
        }
    }
    return answer
}