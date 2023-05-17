function solution(todo_list, finished) {
    var answer = [];
    finished.map((e,idx)=> {
        if(!e) answer.push(todo_list[idx]) })
    return answer;
}