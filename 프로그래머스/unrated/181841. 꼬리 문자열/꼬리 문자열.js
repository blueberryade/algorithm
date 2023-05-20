function solution(str_list, ex) {
    var answer = '';
    str_list.filter(e => !e.includes(ex)).map(e => answer+=e)
    return answer;
}