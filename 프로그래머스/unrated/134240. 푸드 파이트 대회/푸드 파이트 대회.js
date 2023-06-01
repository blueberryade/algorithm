function solution(food) {
    var answer = '';
    food.shift();
    food.forEach((e,i)=> answer += String(i+1).repeat(Math.floor(e/2)))
    return answer+"0"+[...answer].reverse().join("")
}