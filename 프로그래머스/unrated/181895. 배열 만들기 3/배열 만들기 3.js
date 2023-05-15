function solution(arr, intervals) {
    const [one,two] = intervals
    const arr1 = arr.slice(one[0],one[1]+1)
    const arr2 = arr.slice(two[0],two[1]+1)
    var answer = [...arr1,...arr2];
    return answer;
}