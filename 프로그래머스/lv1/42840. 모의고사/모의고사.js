function solution(answers) {
    let answer = [0,0,0];
    const one = [1,2,3,4,5]
    const two = [2,1,2,3,2,4,2,5]
    const three = [3,3,1,1,2,2,4,4,5,5]
    answers.forEach((e,i)=>{
        if(e === one[i%one.length]) answer[0]++
        if(e === two[i%two.length]) answer[1]++
        if(e === three[i%three.length]) answer[2]++
    })
    let max = Math.max(...answer);
    let result = []
    answer.forEach((e,i) =>{
        if(e === max){
            result.push(i+1)
        }
    })
    return result;
}