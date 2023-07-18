function solution(numbers, target) {
    var answer = 0;
    let len = numbers.length;
    function dfs(count,sum){
        if(count===len){
            if(target===sum){
                answer++
            }
            return;
        }
        dfs(count+1,sum+numbers[count])
        dfs(count+1,sum-numbers[count])
    }
    dfs(0,0)
    return answer;
}