function solution(my_string, alp) {
    return [...my_string].map(e => e===alp ? e.toUpperCase() : e).join("")
}