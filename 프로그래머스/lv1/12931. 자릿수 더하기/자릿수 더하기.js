function solution(n)
{
    var answer = String(n).split("").reduce((a,c)=> a + +c,0);
    return answer;
}