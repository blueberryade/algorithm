function solution(nums) {
    let num = nums.length/2
    let set = new Set(nums)
    return set.size < num ? set.size : num;
}