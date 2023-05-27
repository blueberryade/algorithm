function solution(absolutes, signs) {
    var answer = 0;
    signs.forEach((e,i)=> e ? answer+=absolutes[i] : answer-=absolutes[i])
    return answer;
}